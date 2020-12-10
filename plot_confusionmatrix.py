from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

def plot_confusion_matrix(y_true, y_pred,classes,outputfile_dir,confusion_matrix_shape,
                          normalize=False,
                          title=None,
                          cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    # Compute accuracy
    accuracy = accuracy_score(y_true,y_pred)
    if not title:
        if normalize:
            title = 'Normalized confusion matrix'
        else:
            title = 'Accuracy:'+ str(accuracy*100)+'%'
    # Compute confusion matrix
    cm = confusion_matrix(y_true, y_pred,labels=list(range(0,confusion_matrix_shape)))
    # print (cm)
    uncm = cm
    # Only use the labels that appear in the data
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        fig, ax = plt.subplots()
        im = ax.imshow(cm, interpolation='nearest', cmap=cmap)
        ncm = cm
        # print("Normalized confusion matrix")
        # np.savetxt(outputfile_dir+'/ncm.csv', cm, delimiter=',', fmt='%4f')
    else:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        fig, ax = plt.subplots()
        im = ax.imshow(cm, interpolation='nearest', cmap=cmap)
        ncm = cm
        cm = uncm
        # print('Confusion matrix, without normalization')
        # np.savetxt(outputfile_dir+'/cm.csv', cm, delimiter=',', fmt='%d')
    # print(cm)
    
    sum_ = ncm.diagonal()*100
    ncm = ncm * 100
    # Rotate the tick labels and set their alignment.
    plt.setp(ax.get_xticklabels(), rotation=60, ha="right",
             rotation_mode="anchor")
    # print (classes)
    # ax.figure.colorbar(im, ax=ax)
    # We want to show all ticks...
    ax.set(xticks=np.arange(cm.shape[1]),
           yticks=np.arange(cm.shape[0]),
           # ... and label them with the respective list entries
           xticklabels=classes, yticklabels=classes,
           title=title,
           ylabel='True label',
           xlabel='Predicted label')
    # Loop over data dimensions and create text annotations.
    if normalize:  
        fmt = '.2f'
    else:
        fmt = 'd'
    
    # thresh = cm.max() / 2.
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]+1):
            if (j==cm.shape[1]):
                ax.text(j, i, format(sum_[i], '.2f')+'%',
                        ha="left", va="center",
                        color="black", weight="bold")
                        # color="white" if cm[i, j] > thresh else "black")
            elif (i == j and j!= cm.shape[1]):
                ax.text(j, i, format(cm[i, j], fmt),
                        ha="center", va="bottom",
                        color="white", weight="bold")
                        # color="white" if cm[i, j] > thresh else "black")
                ax.text(j, i, format(ncm[i, j], '.2f')+'%',
                        ha="center", va="top",
                        color="white")
                        # color="white" if cm[i, j] > thresh else "black")
            elif (j!= cm.shape[1]):
                ax.text(j, i, format(cm[i, j], fmt),
                    ha="center", va="bottom",
                    color="black", weight="bold")
                ax.text(j, i, format(ncm[i, j], '.2f')+'%',
                    ha="center", va="top",
                    color="black")
        # print (cm[0,15])
    fig.set_size_inches(18, 11)
    fig.tight_layout()
    return ax

plot_confusion_matrix(y_true, y_pred, classes, confusion_matrix_shape=2, title="Confusionmatrix")
