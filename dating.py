#!/usr/bin/env python3
# Created By: Victor Victor-Calixte
# Date: 10/26/26
# This program will determine whether or not the user is valid to date a grandchild based on the asked questions.

import constants


def main():
    # Setting needed variables
    valid_ipt = False

    # Asking the user questions that will validate their worthiness
    is_rich_ipt = input(
        "Is your income well above average? ({0}/{1}): ".format(
            constants.VALID, constants.INVALID
        )
    )
    has_looks_ipt = input(
        "Rate your looks from {0}-{1}: ".format(
            constants.SMALLEST_LOOKS_RANGE, constants.LARGEST_LOOKS_RANGE
        )
    )
    # the try statement will make sure the code safely with invalid user inputs
    try:
        # checking if the IsRich input is valid
        if is_rich_ipt != constants.VALID and is_rich_ipt != constants.INVALID:

            print(constants.ERR_PRINT_MSG)

        else:
            valid_ipt = True

        # This section determines whether or not the user is valid to date the grandchild
        if valid_ipt:
            # Converting the year input to an integer
            has_looks = int(has_looks_ipt)

            if (
                has_looks < constants.SMALLEST_LOOKS_RANGE
                or has_looks > constants.LARGEST_LOOKS_RANGE
            ):
                print(constants.ERR_PRINT_MSG)

            else:
                if is_rich_ipt == constants.VALID:

                    if has_looks > constants.ABV_AVG_LOOKS:

                        print(constants.WORHTY_MSG)

                    else:
                        print(constants.UNWORHTY_MSG)

                else:
                    print(constants.UNWORHTY_MSG)

    except:
        print(constants.ERR_PRINT_MSG)


if __name__ == "__main__":
    main()
