import pandas as pd

from matplotlib import cm
import matplotlib.pyplot as plot
from matplotlib.colors import LinearSegmentedColormap as lcmap
import utils



def plotChartPd(hlabels, ylabel, barLabels, title, valuess, modalidade):
        data = dict()
        fig, ax = plot.subplots(figsize=(11,10))
        for i in range(len(barLabels)):
                data[barLabels[i]] = valuess[i]    


        fig.suptitle(title, fontsize=12)
        #print(data)
        # Dictionary loaded into a DataFrame  
        dataFrame = pd.DataFrame(data, 
                        index=hlabels)
        
        #print(dataFrame)
        stacked_data = dataFrame.apply(lambda x: x*100/sum(x), axis=1)

        newcmp = lcmap('testCmap', segmentdata=utils.cdictNovo, N=256)

        # Draw a vertical bar chart
        ax = stacked_data[barLabels].plot(kind='bar', stacked=True, colormap=newcmp, legend=False, ax=ax)

        ax.set_xticks(range(len(hlabels)))
        ax.tick_params(labelsize=8)
        ax.set_xticklabels(hlabels, rotation = 15, ha="right", rotation_mode="anchor")

        handles, labels = ax.get_legend_handles_labels()
        ax.legend(handles[::-1], labels[::-1],loc='upper left', ncol=1, bbox_to_anchor=(1.05, 1))

        changeSide = True
        for p in ax.patches:
                width, height = p.get_width(), p.get_height()
                if (height > 0.0):                        
                        x, y = p.get_xy()
                        if (height > 1.3):
                                ax.text(x+width/2, 
                                        y+height/2, 
                                        '{:0.2f}%'.format(height), 
                                        horizontalalignment='center', 
                                        verticalalignment='center', 
                                        fontsize=8)
                        else:
                                if (changeSide) :
                                        ax.text(x+width/2, 
                                                y+height/2, 
                                                '{:0.2f}%'.format(height), 
                                                horizontalalignment='left', 
                                                verticalalignment='center', 
                                                fontsize=8)
                                else :
                                        ax.text(x+width/2, 
                                                y+height/2, 
                                                '{:0.2f}%'.format(height), 
                                                horizontalalignment='right', 
                                                verticalalignment='center', 
                                                fontsize=8)
                                
                                changeSide = not (changeSide) 
                        
                        

        fig.tight_layout()
        #plot.show(block=True)
        plot.savefig("./graficos/"+title[0:2] + "_" +modalidade + ".png")
        plot.close(fig)


def plotChartPd2(hlabels, ylabel, barLabels, title, valuess):

        data = dict()
        fig, ax = plot.subplots(figsize=(10,7))
        for i in range(len(valuess)):
                data[barLabels[i]] = valuess[i]

        #print(data)
        # Dictionary loaded into a DataFrame  
        dataFrame = pd.DataFrame(data, 
                        index=hlabels)

        #print(dataFrame)
        
        stacked_data = dataFrame.apply(lambda x: x*100.001/sum(x), axis=1)

        print(stacked_data)

        newcmp = lcmap('testCmap', segmentdata=utils.cdict2, N=256)

        # Draw a vertical bar chart
        ax = stacked_data[['Péssimo',
        'Ruim','Regular','Bom','Ótimo',
        'Desconheço']].plot(kind='bar', title=title, stacked=True, colormap=newcmp, legend=False, ax=ax)

        ax.set_xticks(range(len(hlabels)))
        ax.tick_params(labelsize=12)
        ax.set_xticklabels(hlabels, rotation = 0, ha="right", rotation_mode="anchor")

        handles, labels = ax.get_legend_handles_labels()
        ax.legend(handles[::-1], labels[::-1],loc='upper left', ncol=1, bbox_to_anchor=(1.05, 1))

        for p in ax.patches:
                width, height = p.get_width(), p.get_height()
                x, y = p.get_xy() 
                ax.text(x+width/2, 
                        y+height/2, 
                        '{:0.2f}%'.format(height), 
                        horizontalalignment='center', 
                        verticalalignment='center',
                        size=12)

        fig.tight_layout()
        plot.show(block=True)



def plotChartPd3(hlabels, ylabel, barLabels, title, valuess):

        data = dict()
        fig, ax = plot.subplots(figsize=(10,7))
        for i in range(len(barLabels)):
                data[barLabels[i]] = valuess[i]

        #print(data)
        # Dictionary loaded into a DataFrame  
        dataFrame = pd.DataFrame(data, 
                        index=hlabels)
        
        print(dataFrame)
        stacked_data = dataFrame.apply(lambda x: x*100/sum(x), axis=1)

        newcmp = lcmap('testCmap', segmentdata=utils.cdict, N=256)

        # Draw a vertical bar chart
        ax = stacked_data[['Péssimo',
        'Ruim','Regular','Bom','Ótimo',
        'Inexistente/ Desconheço','Não participei']].plot(kind='bar', title=title, stacked=True, colormap=newcmp, legend=False, ax=ax)

        ax.set_xticks(range(len(hlabels)))
        ax.tick_params(labelsize=8)
        ax.set_xticklabels(hlabels, rotation = 45, ha="right", rotation_mode="anchor")

        handles, labels = ax.get_legend_handles_labels()
        ax.legend(handles[::-1], labels[::-1],loc='upper left', ncol=1, bbox_to_anchor=(1.05, 1))

        for p in ax.patches:
                width, height = p.get_width(), p.get_height()
                x, y = p.get_xy() 
                ax.text(x+width/2, 
                        y+height/2, 
                        '{:0.2f}%'.format(height), 
                        horizontalalignment='center', 
                        verticalalignment='center', 
                        fontsize=8)

        fig.tight_layout()
        plot.show(block=True)

def plotChartPd4(hlabels, ylabel, barLabels, title, valuess):

        data = dict()
        fig, ax = plot.subplots(figsize=(10,7))
        for i in range(len(barLabels)):
                data[barLabels[i]] = valuess[i]

        #print(data)
        # Dictionary loaded into a DataFrame  
        dataFrame = pd.DataFrame(data, 
                        index=hlabels)
        
        print(dataFrame)
        stacked_data = dataFrame.apply(lambda x: x*100/sum(x), axis=1)

        newcmp = lcmap('testCmap', segmentdata=utils.cdict3, N=256)

        # Draw a vertical bar chart
        ax = stacked_data[['Péssimo',
        'Ruim','Regular','Bom','Ótimo',
        'Desconheço','Não participei', 'Não ofertado']].plot(kind='bar', title=title, stacked=True, colormap=newcmp, legend=False, ax=ax)

        ax.set_xticks(range(len(hlabels)))
        ax.tick_params(labelsize=8)
        ax.set_xticklabels(hlabels, rotation = 45, ha="right", rotation_mode="anchor")

        handles, labels = ax.get_legend_handles_labels()
        ax.legend(handles[::-1], labels[::-1],loc='upper left', ncol=1, bbox_to_anchor=(1.05, 1))

        for p in ax.patches:
                width, height = p.get_width(), p.get_height()
                x, y = p.get_xy() 
                ax.text(x+width/2, 
                        y+height/2, 
                        '{:0.2f}%'.format(height), 
                        horizontalalignment='center', 
                        verticalalignment='center', 
                        fontsize=10)

        fig.tight_layout()
        plot.show(block=True)


def plotChartPd5(hlabels, ylabel, barLabels, title, valuess):

        data = dict()
        fig, ax = plot.subplots(figsize=(10,7))
        for i in range(len(valuess)):
                data[barLabels[i]] = valuess[i]

        #print(data)
        # Dictionary loaded into a DataFrame  
        dataFrame = pd.DataFrame(data, 
                        index=hlabels)

        #print(dataFrame)
        
        stacked_data = dataFrame.apply(lambda x: x*100/sum(x), axis=1)

        print(stacked_data)

        newcmp = lcmap('testCmap', segmentdata=utils.cdict2, N=256)

        # Draw a vertical bar chart
        ax = stacked_data[['Péssimo',
        'Ruim','Regular','Bom','Ótimo',
        'Inexistente/Desconheço']].plot(kind='bar', title=title, stacked=True, colormap=newcmp, legend=False, ax=ax)

        ax.set_xticks(range(len(hlabels)))
        ax.tick_params(labelsize=8)
        ax.set_xticklabels(hlabels, rotation = 45, ha="right", rotation_mode="anchor")

        handles, labels = ax.get_legend_handles_labels()
        ax.legend(handles[::-1], labels[::-1],loc='upper left', ncol=1, bbox_to_anchor=(1.05, 1))

        for p in ax.patches:
                width, height = p.get_width(), p.get_height()
                x, y = p.get_xy() 
                ax.text(x+width/2, 
                        y+height/2, 
                        '{:0.2f}%'.format(height), 
                        horizontalalignment='center', 
                        verticalalignment='center',
                        size=10)

        fig.tight_layout()
        plot.show(block=True)


def plotChartPd6(hlabels, ylabel, barLabels, title, valuess):

        data = dict()
        fig, ax = plot.subplots(figsize=(10,7))
        for i in range(len(valuess)):
                data[barLabels[i]] = valuess[i]

        #print(data)
        # Dictionary loaded into a DataFrame  
        dataFrame = pd.DataFrame(data, 
                        index=hlabels)

        #print(dataFrame)
        
        stacked_data = dataFrame.apply(lambda x: x*100/sum(x), axis=1)

        print(stacked_data)

        newcmp = lcmap('testCmap', segmentdata=utils.cdict4, N=256)

        # Draw a vertical bar chart
        ax = stacked_data[['Discordo totalmente',
        'Discordo','Não concordo, nem discordo','Concordo',
        'Concordo totalmente']].plot(kind='bar', title=title, stacked=True, colormap=newcmp, legend=False, ax=ax)

        ax.set_xticks(range(len(hlabels)))
        ax.tick_params(labelsize=8)
        ax.set_xticklabels(hlabels, rotation = 45, ha="right", rotation_mode="anchor")

        handles, labels = ax.get_legend_handles_labels()
        ax.legend(handles[::-1], labels[::-1],loc='upper left', ncol=1, bbox_to_anchor=(1.05, 1))

        for p in ax.patches:
                width, height = p.get_width(), p.get_height()
                x, y = p.get_xy() 
                ax.text(x+width/2, 
                        y+height/2, 
                        '{:0.2f}%'.format(height), 
                        horizontalalignment='center', 
                        verticalalignment='center',
                        size=10)

        fig.tight_layout()
        plot.show(block=True)



def plotChartPd7(hlabels, ylabel, barLabels, title, valuess):

        data = dict()
        fig, ax = plot.subplots(figsize=(10,7))
        for i in range(len(valuess)):
                data[barLabels[i]] = valuess[i]

        #print(data)
        # Dictionary loaded into a DataFrame  
        dataFrame = pd.DataFrame(data, 
                        index=hlabels)

        #print(dataFrame)
        
        stacked_data = dataFrame.apply(lambda x: x*100/sum(x), axis=1)

        print(stacked_data)

        newcmp = lcmap('testCmap', segmentdata=utils.cdict4, N=256)

        # Draw a vertical bar chart
        ax = stacked_data[['Não participei',
        'Pouco participativo','Participação ocasional',
        'Muito participativo','Totalmente participativo']].plot(kind='bar', title=title, stacked=True, colormap=newcmp, legend=False, ax=ax)

        ax.set_xticks(range(len(hlabels)))
        ax.tick_params(labelsize=14)
        ax.set_xticklabels(hlabels, rotation = 45, ha="right", rotation_mode="anchor")

        handles, labels = ax.get_legend_handles_labels()
        ax.legend(handles[::-1], labels[::-1],loc='upper left', ncol=1, bbox_to_anchor=(1.05, 1))

        for p in ax.patches:
                width, height = p.get_width(), p.get_height()
                x, y = p.get_xy() 
                ax.text(x+width/2, 
                        y+height/2, 
                        '{:0.2f}%'.format(height), 
                        horizontalalignment='center', 
                        verticalalignment='center',
                        size=12)

        fig.tight_layout()
        plot.show(block=True)


def plotChartPd8(hlabels, ylabel, barLabels, title, valuess):

        data = dict()
        fig, ax = plot.subplots(figsize=(10,7))
        for i in range(len(valuess)):
                data[barLabels[i]] = valuess[i]

        #print(data)
        # Dictionary loaded into a DataFrame  
        dataFrame = pd.DataFrame(data, 
                        index=hlabels)

        #print(dataFrame)
        
        stacked_data = dataFrame.apply(lambda x: x*100/sum(x), axis=1)

        print(stacked_data)

        newcmp = lcmap('testCmap', segmentdata=utils.cdict3, N=256)

        # Draw a vertical bar chart
        ax = stacked_data[['Péssimo',
        'Ruim','Regular','Bom','Ótimo',
        'Desconheço', 'Não se aplica', 
        'Nunca participei']].plot(kind='bar', title=title, stacked=True, colormap=newcmp, legend=False, ax=ax)

        ax.set_xticks(range(len(hlabels)))
        ax.tick_params(labelsize=12)
        ax.set_xticklabels(hlabels, rotation = 45, ha="right", rotation_mode="anchor")

        handles, labels = ax.get_legend_handles_labels()
        ax.legend(handles[::-1], labels[::-1],loc='upper left', ncol=1, bbox_to_anchor=(1.05, 1))

        for p in ax.patches:
                width, height = p.get_width(), p.get_height()
                x, y = p.get_xy() 
                ax.text(x+width/2, 
                        y+height/2, 
                        '{:0.2f}%'.format(height), 
                        horizontalalignment='center', 
                        verticalalignment='center',
                        size=12)

        fig.tight_layout()
        plot.show(block=True)

def plotChartPd9(hlabels, ylabel, barLabels, title, valuess):

        data = dict()
        fig, ax = plot.subplots(figsize=(10,7))
        for i in range(len(valuess)):
                data[barLabels[i]] = valuess[i]

        #print(data)
        # Dictionary loaded into a DataFrame  
        dataFrame = pd.DataFrame(data, 
                        index=hlabels)

        #print(dataFrame)
        
        stacked_data = dataFrame.apply(lambda x: x*100.001/sum(x), axis=1)

        print(stacked_data)

        newcmp = lcmap('testCmap', segmentdata=utils.cdict, N=256)

        # Draw a vertical bar chart
        ax = stacked_data[['Péssima',
        'Ruim','Regular','Boa','Ótima',
        'Inexistente/Desconheço', 'Não tive acesso']].plot(kind='bar', title=title, stacked=True, colormap=newcmp, legend=False, ax=ax)

        ax.set_xticks(range(len(hlabels)))
        ax.tick_params(labelsize=8)
        ax.set_xticklabels(hlabels, rotation = 45, ha="right", rotation_mode="anchor")

        handles, labels = ax.get_legend_handles_labels()
        ax.legend(handles[::-1], labels[::-1],loc='upper left', ncol=1, bbox_to_anchor=(1.05, 1))

        for p in ax.patches:
                width, height = p.get_width(), p.get_height()
                x, y = p.get_xy() 
                ax.text(x+width/2, 
                        y+height/2, 
                        '{:0.2f}%'.format(height), 
                        horizontalalignment='center', 
                        verticalalignment='center',
                        size=10)

        fig.tight_layout()
        plot.show(block=True)

def plotChartPd10(hlabels, ylabel, barLabels, title, valuess):

        data = dict()
        fig, ax = plot.subplots(figsize=(10,7))
        for i in range(len(valuess)):
                data[barLabels[i]] = valuess[i]

        #print(data)
        # Dictionary loaded into a DataFrame  
        dataFrame = pd.DataFrame(data, 
                        index=hlabels)

        #print(dataFrame)
        
        stacked_data = dataFrame.apply(lambda x: x*100/sum(x), axis=1)

        print(stacked_data)

        newcmp = lcmap('testCmap', segmentdata=utils.cdict2, N=256)

        # Draw a vertical bar chart
        ax = stacked_data[['Discordo totalmente',
        'Discordo','Não concordo, nem discordo','Concordo',
        'Concordo totalmente', 'Desconheço']].plot(kind='bar', title=title, stacked=True, colormap=newcmp, legend=False, ax=ax)

        ax.set_xticks(range(len(hlabels)))
        ax.tick_params(labelsize=8)
        ax.set_xticklabels(hlabels, rotation = 45, ha="right", rotation_mode="anchor")

        handles, labels = ax.get_legend_handles_labels()
        ax.legend(handles[::-1], labels[::-1],loc='upper left', ncol=1, bbox_to_anchor=(1.05, 1))

        for p in ax.patches:
                width, height = p.get_width(), p.get_height()
                x, y = p.get_xy() 
                ax.text(x+width/2, 
                        y+height/2, 
                        '{:0.2f}%'.format(height), 
                        horizontalalignment='center', 
                        verticalalignment='center',
                        size=10)

        fig.tight_layout()
        plot.show(block=True)

def plotChartPd11(hlabels, ylabel, barLabels, title, valuess):

        data = dict()
        fig, ax = plot.subplots(figsize=(10,7))
        for i in range(len(valuess)):
                data[barLabels[i]] = valuess[i]

        #print(data)
        # Dictionary loaded into a DataFrame  
        dataFrame = pd.DataFrame(data, 
                        index=hlabels)

        #print(dataFrame)
        
        stacked_data = dataFrame.apply(lambda x: x*100/sum(x), axis=1)

        print(stacked_data)

        newcmp = lcmap('testCmap', segmentdata=utils.cdict2, N=256)

        # Draw a vertical bar chart
        ax = stacked_data[['Discordo totalmente',
        'Discordo','Não concordo, nem discordo','Concordo',
        'Concordo totalmente', 'Não conheço/Não participo/Não acompanho']].plot(kind='bar', title=title, stacked=True, colormap=newcmp, legend=False, ax=ax)

        ax.set_xticks(range(len(hlabels)))
        ax.tick_params(labelsize=8)
        ax.set_xticklabels(hlabels, rotation = 45, ha="right", rotation_mode="anchor")

        handles, labels = ax.get_legend_handles_labels()
        ax.legend(handles[::-1], labels[::-1],loc='upper left', ncol=1, bbox_to_anchor=(1.05, 1))

        for p in ax.patches:
                width, height = p.get_width(), p.get_height()
                x, y = p.get_xy() 
                ax.text(x+width/2, 
                        y+height/2, 
                        '{:0.2f}%'.format(height), 
                        horizontalalignment='center', 
                        verticalalignment='center',
                        size=10)

        fig.tight_layout()
        plot.show(block=True)