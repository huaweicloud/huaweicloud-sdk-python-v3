# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateDatasourceReqDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'type': 'str',
        'content': 'ContentDetailReq'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'content': 'content'
    }

    def __init__(self, name=None, type=None, content=None):
        """CreateDatasourceReqDTO

        The model defined in huaweicloud sdk

        :param name: 数据源名称
        :type name: str
        :param type: 数据源类型, 包括：IOTDA、API[、OBS、DIS、SMN、FUNCTION_GRAPH、MODEL_ARTS、DCS、KAFKA](tag:IoTA-Cloud-Only)、NODE
        :type type: str
        :param content: 
        :type content: :class:`huaweicloudsdkiotanalytics.v1.ContentDetailReq`
        """
        
        

        self._name = None
        self._type = None
        self._content = None
        self.discriminator = None

        self.name = name
        self.type = type
        self.content = content

    @property
    def name(self):
        """Gets the name of this CreateDatasourceReqDTO.

        数据源名称

        :return: The name of this CreateDatasourceReqDTO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateDatasourceReqDTO.

        数据源名称

        :param name: The name of this CreateDatasourceReqDTO.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        """Gets the type of this CreateDatasourceReqDTO.

        数据源类型, 包括：IOTDA、API[、OBS、DIS、SMN、FUNCTION_GRAPH、MODEL_ARTS、DCS、KAFKA](tag:IoTA-Cloud-Only)、NODE

        :return: The type of this CreateDatasourceReqDTO.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CreateDatasourceReqDTO.

        数据源类型, 包括：IOTDA、API[、OBS、DIS、SMN、FUNCTION_GRAPH、MODEL_ARTS、DCS、KAFKA](tag:IoTA-Cloud-Only)、NODE

        :param type: The type of this CreateDatasourceReqDTO.
        :type type: str
        """
        self._type = type

    @property
    def content(self):
        """Gets the content of this CreateDatasourceReqDTO.

        :return: The content of this CreateDatasourceReqDTO.
        :rtype: :class:`huaweicloudsdkiotanalytics.v1.ContentDetailReq`
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this CreateDatasourceReqDTO.

        :param content: The content of this CreateDatasourceReqDTO.
        :type content: :class:`huaweicloudsdkiotanalytics.v1.ContentDetailReq`
        """
        self._content = content

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
        if not isinstance(other, CreateDatasourceReqDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
