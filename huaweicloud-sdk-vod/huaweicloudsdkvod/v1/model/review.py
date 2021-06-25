# coding: utf-8

import pprint
import re

import six





class Review:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'template_id': 'str',
        'interval': 'int',
        'politics': 'int',
        'terrorism': 'int',
        'porn': 'int'
    }

    attribute_map = {
        'template_id': 'template_id',
        'interval': 'interval',
        'politics': 'politics',
        'terrorism': 'terrorism',
        'porn': 'porn'
    }

    def __init__(self, template_id=None, interval=None, politics=None, terrorism=None, porn=None):
        """Review - a model defined in huaweicloud sdk"""
        
        

        self._template_id = None
        self._interval = None
        self._politics = None
        self._terrorism = None
        self._porn = None
        self.discriminator = None

        self.template_id = template_id
        if interval is not None:
            self.interval = interval
        if politics is not None:
            self.politics = politics
        if terrorism is not None:
            self.terrorism = terrorism
        if porn is not None:
            self.porn = porn

    @property
    def template_id(self):
        """Gets the template_id of this Review.

        审核模板ID

        :return: The template_id of this Review.
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        """Sets the template_id of this Review.

        审核模板ID

        :param template_id: The template_id of this Review.
        :type: str
        """
        self._template_id = template_id

    @property
    def interval(self):
        """Gets the interval of this Review.

        截图的时间间隔。单位为秒

        :return: The interval of this Review.
        :rtype: int
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        """Sets the interval of this Review.

        截图的时间间隔。单位为秒

        :param interval: The interval of this Review.
        :type: int
        """
        self._interval = interval

    @property
    def politics(self):
        """Gets the politics of this Review.

        进行政治人物检测时的置信度。 1）  未传参时表示不进行此项检测。 2）  传 -1 表示采用默认的置信度 

        :return: The politics of this Review.
        :rtype: int
        """
        return self._politics

    @politics.setter
    def politics(self, politics):
        """Sets the politics of this Review.

        进行政治人物检测时的置信度。 1）  未传参时表示不进行此项检测。 2）  传 -1 表示采用默认的置信度 

        :param politics: The politics of this Review.
        :type: int
        """
        self._politics = politics

    @property
    def terrorism(self):
        """Gets the terrorism of this Review.

        进行暴恐元素检测时的置信度。 1)  未传参时表示不进行此项检测。 2)  传 -1 表示采用默认的置信度 

        :return: The terrorism of this Review.
        :rtype: int
        """
        return self._terrorism

    @terrorism.setter
    def terrorism(self, terrorism):
        """Sets the terrorism of this Review.

        进行暴恐元素检测时的置信度。 1)  未传参时表示不进行此项检测。 2)  传 -1 表示采用默认的置信度 

        :param terrorism: The terrorism of this Review.
        :type: int
        """
        self._terrorism = terrorism

    @property
    def porn(self):
        """Gets the porn of this Review.

        进行涉黄内容检测时的置信度。 1)  未传参时表示不进行此项检测。 2)  传 -1 表示采用默认的置信度 

        :return: The porn of this Review.
        :rtype: int
        """
        return self._porn

    @porn.setter
    def porn(self, porn):
        """Sets the porn of this Review.

        进行涉黄内容检测时的置信度。 1)  未传参时表示不进行此项检测。 2)  传 -1 表示采用默认的置信度 

        :param porn: The porn of this Review.
        :type: int
        """
        self._porn = porn

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
        if not isinstance(other, Review):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
