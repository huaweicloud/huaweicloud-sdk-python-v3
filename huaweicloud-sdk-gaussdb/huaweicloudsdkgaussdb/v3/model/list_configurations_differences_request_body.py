# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListConfigurationsDifferencesRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'source_configuration_id': 'str',
        'target_configuration_id': 'str'
    }

    attribute_map = {
        'source_configuration_id': 'source_configuration_id',
        'target_configuration_id': 'target_configuration_id'
    }

    def __init__(self, source_configuration_id=None, target_configuration_id=None):
        """ListConfigurationsDifferencesRequestBody

        The model defined in huaweicloud sdk

        :param source_configuration_id: 需要进行比较的源参数模板ID。  通过调用[查询参数模板](https://support.huaweicloud.com/api-gaussdbformysql/ListGaussMySqlConfigurations.html)接口获取。  请求响应成功后在响应消息体中包含的“id”的值即为source_configuration_id值。
        :type source_configuration_id: str
        :param target_configuration_id: 需要进行比较的目标参数模板ID。  通过调用[查询参数模板](https://support.huaweicloud.com/api-gaussdbformysql/ListGaussMySqlConfigurations.html)接口获取。  请求响应成功后在响应消息体中包含的“id”的值即为target_configuration_id值。
        :type target_configuration_id: str
        """
        
        

        self._source_configuration_id = None
        self._target_configuration_id = None
        self.discriminator = None

        self.source_configuration_id = source_configuration_id
        self.target_configuration_id = target_configuration_id

    @property
    def source_configuration_id(self):
        """Gets the source_configuration_id of this ListConfigurationsDifferencesRequestBody.

        需要进行比较的源参数模板ID。  通过调用[查询参数模板](https://support.huaweicloud.com/api-gaussdbformysql/ListGaussMySqlConfigurations.html)接口获取。  请求响应成功后在响应消息体中包含的“id”的值即为source_configuration_id值。

        :return: The source_configuration_id of this ListConfigurationsDifferencesRequestBody.
        :rtype: str
        """
        return self._source_configuration_id

    @source_configuration_id.setter
    def source_configuration_id(self, source_configuration_id):
        """Sets the source_configuration_id of this ListConfigurationsDifferencesRequestBody.

        需要进行比较的源参数模板ID。  通过调用[查询参数模板](https://support.huaweicloud.com/api-gaussdbformysql/ListGaussMySqlConfigurations.html)接口获取。  请求响应成功后在响应消息体中包含的“id”的值即为source_configuration_id值。

        :param source_configuration_id: The source_configuration_id of this ListConfigurationsDifferencesRequestBody.
        :type source_configuration_id: str
        """
        self._source_configuration_id = source_configuration_id

    @property
    def target_configuration_id(self):
        """Gets the target_configuration_id of this ListConfigurationsDifferencesRequestBody.

        需要进行比较的目标参数模板ID。  通过调用[查询参数模板](https://support.huaweicloud.com/api-gaussdbformysql/ListGaussMySqlConfigurations.html)接口获取。  请求响应成功后在响应消息体中包含的“id”的值即为target_configuration_id值。

        :return: The target_configuration_id of this ListConfigurationsDifferencesRequestBody.
        :rtype: str
        """
        return self._target_configuration_id

    @target_configuration_id.setter
    def target_configuration_id(self, target_configuration_id):
        """Sets the target_configuration_id of this ListConfigurationsDifferencesRequestBody.

        需要进行比较的目标参数模板ID。  通过调用[查询参数模板](https://support.huaweicloud.com/api-gaussdbformysql/ListGaussMySqlConfigurations.html)接口获取。  请求响应成功后在响应消息体中包含的“id”的值即为target_configuration_id值。

        :param target_configuration_id: The target_configuration_id of this ListConfigurationsDifferencesRequestBody.
        :type target_configuration_id: str
        """
        self._target_configuration_id = target_configuration_id

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
        if not isinstance(other, ListConfigurationsDifferencesRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
