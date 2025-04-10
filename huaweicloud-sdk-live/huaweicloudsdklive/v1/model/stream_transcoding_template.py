# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StreamTranscodingTemplate:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain': 'str',
        'app_name': 'str',
        'trans_type': 'str',
        'quality_info': 'list[QualityInfo]'
    }

    attribute_map = {
        'domain': 'domain',
        'app_name': 'app_name',
        'trans_type': 'trans_type',
        'quality_info': 'quality_info'
    }

    def __init__(self, domain=None, app_name=None, trans_type=None, quality_info=None):
        r"""StreamTranscodingTemplate

        The model defined in huaweicloud sdk

        :param domain: 推流域名
        :type domain: str
        :param app_name: 应用名称。 默认为“live”，若您需要自定义应用名称，请先提交工单申请。 
        :type app_name: str
        :param trans_type: 转码流触发模式。 - play：拉流触发转码。 - publish：推流触发转码。 默认为play 
        :type trans_type: str
        :param quality_info: 视频质量信息
        :type quality_info: list[:class:`huaweicloudsdklive.v1.QualityInfo`]
        """
        
        

        self._domain = None
        self._app_name = None
        self._trans_type = None
        self._quality_info = None
        self.discriminator = None

        self.domain = domain
        self.app_name = app_name
        if trans_type is not None:
            self.trans_type = trans_type
        self.quality_info = quality_info

    @property
    def domain(self):
        r"""Gets the domain of this StreamTranscodingTemplate.

        推流域名

        :return: The domain of this StreamTranscodingTemplate.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        r"""Sets the domain of this StreamTranscodingTemplate.

        推流域名

        :param domain: The domain of this StreamTranscodingTemplate.
        :type domain: str
        """
        self._domain = domain

    @property
    def app_name(self):
        r"""Gets the app_name of this StreamTranscodingTemplate.

        应用名称。 默认为“live”，若您需要自定义应用名称，请先提交工单申请。 

        :return: The app_name of this StreamTranscodingTemplate.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        r"""Sets the app_name of this StreamTranscodingTemplate.

        应用名称。 默认为“live”，若您需要自定义应用名称，请先提交工单申请。 

        :param app_name: The app_name of this StreamTranscodingTemplate.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def trans_type(self):
        r"""Gets the trans_type of this StreamTranscodingTemplate.

        转码流触发模式。 - play：拉流触发转码。 - publish：推流触发转码。 默认为play 

        :return: The trans_type of this StreamTranscodingTemplate.
        :rtype: str
        """
        return self._trans_type

    @trans_type.setter
    def trans_type(self, trans_type):
        r"""Sets the trans_type of this StreamTranscodingTemplate.

        转码流触发模式。 - play：拉流触发转码。 - publish：推流触发转码。 默认为play 

        :param trans_type: The trans_type of this StreamTranscodingTemplate.
        :type trans_type: str
        """
        self._trans_type = trans_type

    @property
    def quality_info(self):
        r"""Gets the quality_info of this StreamTranscodingTemplate.

        视频质量信息

        :return: The quality_info of this StreamTranscodingTemplate.
        :rtype: list[:class:`huaweicloudsdklive.v1.QualityInfo`]
        """
        return self._quality_info

    @quality_info.setter
    def quality_info(self, quality_info):
        r"""Sets the quality_info of this StreamTranscodingTemplate.

        视频质量信息

        :param quality_info: The quality_info of this StreamTranscodingTemplate.
        :type quality_info: list[:class:`huaweicloudsdklive.v1.QualityInfo`]
        """
        self._quality_info = quality_info

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
        if not isinstance(other, StreamTranscodingTemplate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
