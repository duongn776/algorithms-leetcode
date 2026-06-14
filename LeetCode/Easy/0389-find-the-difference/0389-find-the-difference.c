char findTheDifference(char* s, char* t) {
    int counts[26] = {0};

    for (int i = 0; s[i] != '\0'; i++)
    {
        counts[s[i] -'a']++;
    }

    for (int i = 0; t[i] != '\0'; i++)
    {
        counts[t[i] -'a']--;
        if (counts[t[i] - 'a'] < 0)
        {
            return t[i];
        }
    }

    return 0;
}