# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowInstanceExtendProductInfoRespHourly:

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
        'version': 'str',
        'values': 'list[ListProductsRespValues]'
    }

    attribute_map = {
        'name': 'name',
        'version': 'version',
        'values': 'values'
    }

    def __init__(self, name=None, version=None, values=None):
        r"""ShowInstanceExtendProductInfoRespHourly

        The model defined in huaweicloud sdk

        :param name: 消息引擎的名称，该字段显示为rabbitmq。
        :type name: str
        :param version: 消息引擎的版本，当前支持3.8.35[和3.7.17](tag:hk_sbc,sbc)。
        :type version: str
        :param values: 产品规格列表。
        :type values: list[:class:`huaweicloudsdkrabbitmq.v2.ListProductsRespValues`]
        """
        
        

        self._name = None
        self._version = None
        self._values = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if version is not None:
            self.version = version
        if values is not None:
            self.values = values

    @property
    def name(self):
        r"""Gets the name of this ShowInstanceExtendProductInfoRespHourly.

        消息引擎的名称，该字段显示为rabbitmq。

        :return: The name of this ShowInstanceExtendProductInfoRespHourly.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowInstanceExtendProductInfoRespHourly.

        消息引擎的名称，该字段显示为rabbitmq。

        :param name: The name of this ShowInstanceExtendProductInfoRespHourly.
        :type name: str
        """
        self._name = name

    @property
    def version(self):
        r"""Gets the version of this ShowInstanceExtendProductInfoRespHourly.

        消息引擎的版本，当前支持3.8.35[和3.7.17](tag:hk_sbc,sbc)。

        :return: The version of this ShowInstanceExtendProductInfoRespHourly.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this ShowInstanceExtendProductInfoRespHourly.

        消息引擎的版本，当前支持3.8.35[和3.7.17](tag:hk_sbc,sbc)。

        :param version: The version of this ShowInstanceExtendProductInfoRespHourly.
        :type version: str
        """
        self._version = version

    @property
    def values(self):
        r"""Gets the values of this ShowInstanceExtendProductInfoRespHourly.

        产品规格列表。

        :return: The values of this ShowInstanceExtendProductInfoRespHourly.
        :rtype: list[:class:`huaweicloudsdkrabbitmq.v2.ListProductsRespValues`]
        """
        return self._values

    @values.setter
    def values(self, values):
        r"""Sets the values of this ShowInstanceExtendProductInfoRespHourly.

        产品规格列表。

        :param values: The values of this ShowInstanceExtendProductInfoRespHourly.
        :type values: list[:class:`huaweicloudsdkrabbitmq.v2.ListProductsRespValues`]
        """
        self._values = values

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
        if not isinstance(other, ShowInstanceExtendProductInfoRespHourly):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
