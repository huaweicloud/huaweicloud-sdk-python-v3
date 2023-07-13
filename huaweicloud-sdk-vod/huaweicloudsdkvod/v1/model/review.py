# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


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
        """Review

        The model defined in huaweicloud sdk

        :param template_id: 审核模板ID。您可以在视频点播控制台配置审核模板后获取，具体请参见[审核设置](https://support.huaweicloud.com/usermanual-vod/vod_01_0057.html)。
        :type template_id: str
        :param interval: 截图检测时间间隔，取值范围为[0,100]，该参数在请求参数中忽略。
        :type interval: int
        :param politics: 鉴政内容检测置信度，取值范围为[0,100]，该参数在请求参数中忽略。 置信度越高，说明审核结果越可信。未开启或设置为0时，表示未进行此项检测。
        :type politics: int
        :param terrorism: 鉴恐内容的检测置信度，取值范围为[0,100]，该参数在请求参数中忽略。 置信度越高，说明审核结果越可信。未开启或设置为0时，表示未进行此项检测。
        :type terrorism: int
        :param porn: 鉴黄内容的检测置信度，取值范围为[0,100]，该参数在请求参数中忽略。 置信度越高，说明审核结果越可信。未开启或设置为0时，表示未进行此项检测。  
        :type porn: int
        """
        
        

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

        审核模板ID。您可以在视频点播控制台配置审核模板后获取，具体请参见[审核设置](https://support.huaweicloud.com/usermanual-vod/vod_01_0057.html)。

        :return: The template_id of this Review.
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        """Sets the template_id of this Review.

        审核模板ID。您可以在视频点播控制台配置审核模板后获取，具体请参见[审核设置](https://support.huaweicloud.com/usermanual-vod/vod_01_0057.html)。

        :param template_id: The template_id of this Review.
        :type template_id: str
        """
        self._template_id = template_id

    @property
    def interval(self):
        """Gets the interval of this Review.

        截图检测时间间隔，取值范围为[0,100]，该参数在请求参数中忽略。

        :return: The interval of this Review.
        :rtype: int
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        """Sets the interval of this Review.

        截图检测时间间隔，取值范围为[0,100]，该参数在请求参数中忽略。

        :param interval: The interval of this Review.
        :type interval: int
        """
        self._interval = interval

    @property
    def politics(self):
        """Gets the politics of this Review.

        鉴政内容检测置信度，取值范围为[0,100]，该参数在请求参数中忽略。 置信度越高，说明审核结果越可信。未开启或设置为0时，表示未进行此项检测。

        :return: The politics of this Review.
        :rtype: int
        """
        return self._politics

    @politics.setter
    def politics(self, politics):
        """Sets the politics of this Review.

        鉴政内容检测置信度，取值范围为[0,100]，该参数在请求参数中忽略。 置信度越高，说明审核结果越可信。未开启或设置为0时，表示未进行此项检测。

        :param politics: The politics of this Review.
        :type politics: int
        """
        self._politics = politics

    @property
    def terrorism(self):
        """Gets the terrorism of this Review.

        鉴恐内容的检测置信度，取值范围为[0,100]，该参数在请求参数中忽略。 置信度越高，说明审核结果越可信。未开启或设置为0时，表示未进行此项检测。

        :return: The terrorism of this Review.
        :rtype: int
        """
        return self._terrorism

    @terrorism.setter
    def terrorism(self, terrorism):
        """Sets the terrorism of this Review.

        鉴恐内容的检测置信度，取值范围为[0,100]，该参数在请求参数中忽略。 置信度越高，说明审核结果越可信。未开启或设置为0时，表示未进行此项检测。

        :param terrorism: The terrorism of this Review.
        :type terrorism: int
        """
        self._terrorism = terrorism

    @property
    def porn(self):
        """Gets the porn of this Review.

        鉴黄内容的检测置信度，取值范围为[0,100]，该参数在请求参数中忽略。 置信度越高，说明审核结果越可信。未开启或设置为0时，表示未进行此项检测。  

        :return: The porn of this Review.
        :rtype: int
        """
        return self._porn

    @porn.setter
    def porn(self, porn):
        """Sets the porn of this Review.

        鉴黄内容的检测置信度，取值范围为[0,100]，该参数在请求参数中忽略。 置信度越高，说明审核结果越可信。未开启或设置为0时，表示未进行此项检测。  

        :param porn: The porn of this Review.
        :type porn: int
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
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Review):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
