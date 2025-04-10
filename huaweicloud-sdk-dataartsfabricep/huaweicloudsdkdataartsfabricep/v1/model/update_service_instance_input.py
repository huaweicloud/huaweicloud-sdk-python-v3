# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateServiceInstanceInput:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'source': 'SourceRef',
        'name': 'str',
        'description': 'str',
        'config': 'UpdateServiceInstanceConfig'
    }

    attribute_map = {
        'source': 'source',
        'name': 'name',
        'description': 'description',
        'config': 'config'
    }

    def __init__(self, source=None, name=None, description=None, config=None):
        r"""UpdateServiceInstanceInput

        The model defined in huaweicloud sdk

        :param source: 
        :type source: :class:`huaweicloudsdkdataartsfabricep.v1.SourceRef`
        :param name: 一个Service Instance的名称，只能包含中文、字母、数字、下划线、中划线、点、空格
        :type name: str
        :param description: 描述信息
        :type description: str
        :param config: 
        :type config: :class:`huaweicloudsdkdataartsfabricep.v1.UpdateServiceInstanceConfig`
        """
        
        

        self._source = None
        self._name = None
        self._description = None
        self._config = None
        self.discriminator = None

        if source is not None:
            self.source = source
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if config is not None:
            self.config = config

    @property
    def source(self):
        r"""Gets the source of this UpdateServiceInstanceInput.

        :return: The source of this UpdateServiceInstanceInput.
        :rtype: :class:`huaweicloudsdkdataartsfabricep.v1.SourceRef`
        """
        return self._source

    @source.setter
    def source(self, source):
        r"""Sets the source of this UpdateServiceInstanceInput.

        :param source: The source of this UpdateServiceInstanceInput.
        :type source: :class:`huaweicloudsdkdataartsfabricep.v1.SourceRef`
        """
        self._source = source

    @property
    def name(self):
        r"""Gets the name of this UpdateServiceInstanceInput.

        一个Service Instance的名称，只能包含中文、字母、数字、下划线、中划线、点、空格

        :return: The name of this UpdateServiceInstanceInput.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UpdateServiceInstanceInput.

        一个Service Instance的名称，只能包含中文、字母、数字、下划线、中划线、点、空格

        :param name: The name of this UpdateServiceInstanceInput.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this UpdateServiceInstanceInput.

        描述信息

        :return: The description of this UpdateServiceInstanceInput.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdateServiceInstanceInput.

        描述信息

        :param description: The description of this UpdateServiceInstanceInput.
        :type description: str
        """
        self._description = description

    @property
    def config(self):
        r"""Gets the config of this UpdateServiceInstanceInput.

        :return: The config of this UpdateServiceInstanceInput.
        :rtype: :class:`huaweicloudsdkdataartsfabricep.v1.UpdateServiceInstanceConfig`
        """
        return self._config

    @config.setter
    def config(self, config):
        r"""Sets the config of this UpdateServiceInstanceInput.

        :param config: The config of this UpdateServiceInstanceInput.
        :type config: :class:`huaweicloudsdkdataartsfabricep.v1.UpdateServiceInstanceConfig`
        """
        self._config = config

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
        if not isinstance(other, UpdateServiceInstanceInput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
