# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListYmlsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'configurations': 'object'
    }

    attribute_map = {
        'configurations': 'configurations'
    }

    def __init__(self, configurations=None):
        """ListYmlsResponse

        The model defined in huaweicloud sdk

        :param configurations: 集群参数配置列表。该对象中key值以具体获取为准，value拥有以下属性。 - id:  参数配置ID。 - key: 参数名称。 - vlaue:  参数值。 - defaultValue:  参数默认值。 - regex:  参数约束限制。 - desc:  参数中文描述。 - type:  参数类型描述。 - moduleDesc: 参数功能中文描述。 - modifyEnable: 参数是否可修改 true： 可以修改。 false：不可修改。 - enableValue: 参数支持修改的值。 - fileName: 参数存在的文件名称。默认为elasticsearch.yml。 - version:  版本信息。 - descENG: 参数英文描述。 - moduleDescENG:  参数功能英文描述。
        :type configurations: object
        """
        
        super(ListYmlsResponse, self).__init__()

        self._configurations = None
        self.discriminator = None

        if configurations is not None:
            self.configurations = configurations

    @property
    def configurations(self):
        """Gets the configurations of this ListYmlsResponse.

        集群参数配置列表。该对象中key值以具体获取为准，value拥有以下属性。 - id:  参数配置ID。 - key: 参数名称。 - vlaue:  参数值。 - defaultValue:  参数默认值。 - regex:  参数约束限制。 - desc:  参数中文描述。 - type:  参数类型描述。 - moduleDesc: 参数功能中文描述。 - modifyEnable: 参数是否可修改 true： 可以修改。 false：不可修改。 - enableValue: 参数支持修改的值。 - fileName: 参数存在的文件名称。默认为elasticsearch.yml。 - version:  版本信息。 - descENG: 参数英文描述。 - moduleDescENG:  参数功能英文描述。

        :return: The configurations of this ListYmlsResponse.
        :rtype: object
        """
        return self._configurations

    @configurations.setter
    def configurations(self, configurations):
        """Sets the configurations of this ListYmlsResponse.

        集群参数配置列表。该对象中key值以具体获取为准，value拥有以下属性。 - id:  参数配置ID。 - key: 参数名称。 - vlaue:  参数值。 - defaultValue:  参数默认值。 - regex:  参数约束限制。 - desc:  参数中文描述。 - type:  参数类型描述。 - moduleDesc: 参数功能中文描述。 - modifyEnable: 参数是否可修改 true： 可以修改。 false：不可修改。 - enableValue: 参数支持修改的值。 - fileName: 参数存在的文件名称。默认为elasticsearch.yml。 - version:  版本信息。 - descENG: 参数英文描述。 - moduleDescENG:  参数功能英文描述。

        :param configurations: The configurations of this ListYmlsResponse.
        :type configurations: object
        """
        self._configurations = configurations

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
        if not isinstance(other, ListYmlsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
