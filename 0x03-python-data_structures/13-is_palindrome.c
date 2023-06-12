#include "lists.h"

/**
 * is_palindrome - Checks if a singly linked list is a palindrome
 * @head: Double pointer to the head of the linked list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 * An empty list is considered a palindrome
 */
int is_palindrome(listint_t **head)
{
	int array[99999], i = 0, j = 0, ls_sz = 0;
	listint_t *aux;

	if (head == NULL || (*head) == NULL)
		return (1);
	aux = *head;
	while (aux != NULL)
	{
		array[i] = aux->n;
		aux = aux->next;
		i++;
	}
	i -= 1;
	if (i % 2 != 0)
		ls_sz = (i + 1) / 2;
	else
		ls_sz = i / 2;
	while (j < ls_sz)
	{
		if (array[j] != array[i])
			return (0);
		i--;
		j++;
	}
	return (1);
}
