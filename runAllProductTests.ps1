# Define the values for each product
# $colorValues = 0, 8, 16, 24
# $bookValues = 0, 5, 10, 15
$colorValues = 0, 8
$bookValues = 0, 5

# Loop through all combinations of values for each product
foreach ($azul in $colorValues) {
    foreach ($rosa in $colorValues) {
        foreach ($laranja in $colorValues) {
            foreach ($verde in $colorValues) {
                foreach ($livro in $bookValues) {
                    # Construct the command with the current combination of values
                    $command = "python .\testTidio.py --azul $azul --rosa $rosa --laranja $laranja --verde $verde --livro $livro"
                    Write-Output "Running: $command"
                    # Execute the command
                    Invoke-Expression $command
                }
            }
        }
    }
}
