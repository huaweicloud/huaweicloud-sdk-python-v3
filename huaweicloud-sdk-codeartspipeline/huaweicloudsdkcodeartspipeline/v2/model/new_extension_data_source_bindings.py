# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NewExtensionDataSourceBindings:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'target': 'str',
        'endpoint_id': 'str',
        'data_source_name': 'str'
    }

    attribute_map = {
        'target': 'target',
        'endpoint_id': 'endpointId',
        'data_source_name': 'data_source_name'
    }

    def __init__(self, target=None, endpoint_id=None, data_source_name=None):
        r"""NewExtensionDataSourceBindings

        The model defined in huaweicloud sdk

        :param target: **参数解释**： 目标地址。 **取值范围**： 不涉及。 
        :type target: str
        :param endpoint_id: **参数解释**： 扩展点id。 **取值范围**： 不涉及。 
        :type endpoint_id: str
        :param data_source_name: **参数解释**： 数据源绑定名称。 **取值范围**： 不涉及。 
        :type data_source_name: str
        """
        
        

        self._target = None
        self._endpoint_id = None
        self._data_source_name = None
        self.discriminator = None

        if target is not None:
            self.target = target
        if endpoint_id is not None:
            self.endpoint_id = endpoint_id
        if data_source_name is not None:
            self.data_source_name = data_source_name

    @property
    def target(self):
        r"""Gets the target of this NewExtensionDataSourceBindings.

        **参数解释**： 目标地址。 **取值范围**： 不涉及。 

        :return: The target of this NewExtensionDataSourceBindings.
        :rtype: str
        """
        return self._target

    @target.setter
    def target(self, target):
        r"""Sets the target of this NewExtensionDataSourceBindings.

        **参数解释**： 目标地址。 **取值范围**： 不涉及。 

        :param target: The target of this NewExtensionDataSourceBindings.
        :type target: str
        """
        self._target = target

    @property
    def endpoint_id(self):
        r"""Gets the endpoint_id of this NewExtensionDataSourceBindings.

        **参数解释**： 扩展点id。 **取值范围**： 不涉及。 

        :return: The endpoint_id of this NewExtensionDataSourceBindings.
        :rtype: str
        """
        return self._endpoint_id

    @endpoint_id.setter
    def endpoint_id(self, endpoint_id):
        r"""Sets the endpoint_id of this NewExtensionDataSourceBindings.

        **参数解释**： 扩展点id。 **取值范围**： 不涉及。 

        :param endpoint_id: The endpoint_id of this NewExtensionDataSourceBindings.
        :type endpoint_id: str
        """
        self._endpoint_id = endpoint_id

    @property
    def data_source_name(self):
        r"""Gets the data_source_name of this NewExtensionDataSourceBindings.

        **参数解释**： 数据源绑定名称。 **取值范围**： 不涉及。 

        :return: The data_source_name of this NewExtensionDataSourceBindings.
        :rtype: str
        """
        return self._data_source_name

    @data_source_name.setter
    def data_source_name(self, data_source_name):
        r"""Sets the data_source_name of this NewExtensionDataSourceBindings.

        **参数解释**： 数据源绑定名称。 **取值范围**： 不涉及。 

        :param data_source_name: The data_source_name of this NewExtensionDataSourceBindings.
        :type data_source_name: str
        """
        self._data_source_name = data_source_name

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
        if not isinstance(other, NewExtensionDataSourceBindings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
