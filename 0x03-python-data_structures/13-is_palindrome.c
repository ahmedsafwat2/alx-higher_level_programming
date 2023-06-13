#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: A pointer to the head of the linked list.
 *
 * Return: If the linked list is not a palindrome - 0.
 *         If the linked list is a palindrome - 1.
 */
int is_palindrome(listint_t **head)
{
	listint_t *current;
	int n, i, flag, j, *a;

	current = *head;
	n = 0;
	while (current != NULL)
	{
		current = current->next;
		n++;
	}
	current = *head;
	a = malloc(n * sizeof(int));
	for (i = 0; i < n; i++)
	{
		a[i] = current->n;
		current = current->next;
	}
	for (i = 0, j = n - 1; i < n / 2 && j >= n / 2; i++, j--)
	{
		if (a[i] != a[j])
		{
			flag = 1;
			break;
		}
	}
	if (flag == 1)
	{
		free(a);
		return (0);
	}
	else
	{
		free(a);
		return (1);
	}
}
