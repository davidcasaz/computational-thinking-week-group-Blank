using DataFrames, CSV, Statistics

# Define paths to input and output files
input_path = joinpath("fulldata", "data3.csv")
output_path = joinpath("fulldata", "data4.txt")

# Read the CSV file into a DataFrame
people_df = CSV.File(input_path) |> DataFrame

# Function to classify a score based on quartiles
function classify_score(score, quartiles)
    if score <= quartiles[1]
        return "low"
    elseif score <= quartiles[2]
        return "middle"
    elseif score <= quartiles[3]
        return "good"
    else
        return "super"
    end
end

# Iterate over each column (skipping the 'Name' column)
for col_name in names(people_df)[2:end]
    # Convert float values that are whole numbers to integers
    col_data = map(x -> isa(x, Float64) && x == floor(x) ? Int(x) : x, people_df[!, col_name])

    # Keep only numeric data for quartile calculations
    valid_data = filter(x -> x isa Number, col_data)

    if isempty(valid_data)
        println("No valid data for column $col_name")
        continue
    end

    # Calculate quartiles for the column
    quartiles = quantile(valid_data, [0.25, 0.5, 0.75])

    # Apply classification to all values (skip missing or non-numeric entries)
    new_col = map(x -> x isa Number ? classify_score(x, quartiles) : "low", col_data)

    # Replace the column with the classified values
    people_df[!, col_name] = new_col
end

# Save the modified DataFrame to a new TXT file inside fulldata
CSV.write(output_path, people_df)

println("✅ Processed file saved to: $output_path")
