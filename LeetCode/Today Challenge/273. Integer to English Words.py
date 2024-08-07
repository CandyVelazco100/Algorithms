273. Integer to English Words
Convert a non-negative integer num to its English words representation.

class Solution:
        def numberToWords(self, num: int) -> str:
            if num == 0:
                return 'Zero'

            lt20 = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine',
                    'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen',
                    'Seventeen', 'Eighteen', 'Nineteen']

            tens = ['', 'Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']

            thousands = ['Billion', 'Million', 'Thousand', '']

            # Helper function to convert a number less than 1000 to words
            def translate(num):
                if num == 0:
                    return ''
                elif num < 20:
                    return lt20[num - 1] + ' '
                elif num < 100:
                    return tens[num // 10] + ' ' + translate(num % 10)
                else:
                    return lt20[num // 100 - 1] + ' Hundred ' + translate(num % 100)
            
            result = []  # List to store the parts of the result string
            i, j = 1000000000, 0  # Initialize the divisor for the highest unit (billion) and the index for units

            # Loop to handle each unit position from billion down to ones
            while i > 0:
                if num // i != 0:
                    result.append(translate(num // i))  # Convert the current unit position to words
                    if thousands[j]:  # Only add the unit name if it is non-empty
                        result.append(thousands[j])  # Add the unit name (Billion, Million, ...)
                    result.append(' ')  # Add space after the unit name
                    num %= i  # Update the number, removing the current unit portion
                j += 1  # Increment the index for units
                i //= 1000  # Move to the next unit (from billion to million to thousand to ones)
            
            return ''.join(result).strip()  # Join the parts and remove any extra spaces
