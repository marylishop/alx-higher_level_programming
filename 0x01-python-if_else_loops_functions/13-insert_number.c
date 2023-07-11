#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: pointer to the head of the list
 * @number: number to store in the new node
 * Return: pointer to the new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = malloc(sizeof(listint_t));
	listint_t *current = *head;
	listint_t *prev = NULL;

	if (!new_node)
	return (NULL);

	new_node->n = number;
	new_node->next = NULL;

	if (!*head)
{
	*head = new_node;
	return (new_node);
}

	while (current && current->n < number)
{
	prev = current;
	current = current->next;
}

	if (!prev)
	{
	new_node->next = *head;
	*head = new_node;
}
	else
{
	prev->next = new_node;
	new_node->next = current;
}

	return (new_node);
}
