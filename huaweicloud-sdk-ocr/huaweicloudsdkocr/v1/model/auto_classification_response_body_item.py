# coding: utf-8

import pprint
import re

import six





class AutoClassificationResponseBodyItem:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'status': 'object',
        'content': 'object',
        'type': 'str',
        'location': 'list[int]',
        'confidence': 'object'
    }

    attribute_map = {
        'status': 'status',
        'content': 'content',
        'type': 'type',
        'location': 'location',
        'confidence': 'confidence'
    }

    def __init__(self, status=None, content=None, type=None, location=None, confidence=None):
        """AutoClassificationResponseBodyItem - a model defined in huaweicloud sdk"""
        
        

        self._status = None
        self._content = None
        self._type = None
        self._location = None
        self._confidence = None
        self.discriminator = None

        self.status = status
        self.content = content
        self.type = type
        self.location = location
        if confidence is not None:
            self.confidence = confidence

    @property
    def status(self):
        """Gets the status of this AutoClassificationResponseBodyItem.

        指示各对应票证的识别状态。  

        :return: The status of this AutoClassificationResponseBodyItem.
        :rtype: object
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this AutoClassificationResponseBodyItem.

        指示各对应票证的识别状态。  

        :param status: The status of this AutoClassificationResponseBodyItem.
        :type: object
        """
        self._status = status

    @property
    def content(self):
        """Gets the content of this AutoClassificationResponseBodyItem.

        对应票证具体结构化识别的结果。 

        :return: The content of this AutoClassificationResponseBodyItem.
        :rtype: object
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this AutoClassificationResponseBodyItem.

        对应票证具体结构化识别的结果。 

        :param content: The content of this AutoClassificationResponseBodyItem.
        :type: object
        """
        self._content = content

    @property
    def type(self):
        """Gets the type of this AutoClassificationResponseBodyItem.

        对应票证的类别。         

        :return: The type of this AutoClassificationResponseBodyItem.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AutoClassificationResponseBodyItem.

        对应票证的类别。         

        :param type: The type of this AutoClassificationResponseBodyItem.
        :type: str
        """
        self._type = type

    @property
    def location(self):
        """Gets the location of this AutoClassificationResponseBodyItem.

        文字块的区域位置信息，列表形式，包含文字区域四个顶点的二维坐标（x,y）;坐标原点为图片左上角，x轴沿水平方向，y轴沿竖直方向。 

        :return: The location of this AutoClassificationResponseBodyItem.
        :rtype: list[int]
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this AutoClassificationResponseBodyItem.

        文字块的区域位置信息，列表形式，包含文字区域四个顶点的二维坐标（x,y）;坐标原点为图片左上角，x轴沿水平方向，y轴沿竖直方向。 

        :param location: The location of this AutoClassificationResponseBodyItem.
        :type: list[int]
        """
        self._location = location

    @property
    def confidence(self):
        """Gets the confidence of this AutoClassificationResponseBodyItem.

        相关字段的置信度信息，置信度越大，表示本次识别的对应字段的可靠性越高，在统计意义上，置信度越大，准确率越高。 置信度由算法给出，不直接等价于对应字段的准确率。          

        :return: The confidence of this AutoClassificationResponseBodyItem.
        :rtype: object
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """Sets the confidence of this AutoClassificationResponseBodyItem.

        相关字段的置信度信息，置信度越大，表示本次识别的对应字段的可靠性越高，在统计意义上，置信度越大，准确率越高。 置信度由算法给出，不直接等价于对应字段的准确率。          

        :param confidence: The confidence of this AutoClassificationResponseBodyItem.
        :type: object
        """
        self._confidence = confidence

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                if attr in self.sensitive_list:
                    result[attr] = "****"
                else:
                    result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AutoClassificationResponseBodyItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
