# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchUpgradeDatabasesRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'databases_instance_infos': 'list[UpgradeDatabasesSingleInstance]',
        'delay': 'str'
    }

    attribute_map = {
        'databases_instance_infos': 'databases_instance_infos',
        'delay': 'delay'
    }

    def __init__(self, databases_instance_infos=None, delay=None):
        r"""BatchUpgradeDatabasesRequestBody

        The model defined in huaweicloud sdk

        :param databases_instance_infos: 要版本升级的批量实例。
        :type databases_instance_infos: list[:class:`huaweicloudsdkgaussdb.v3.UpgradeDatabasesSingleInstance`]
        :param delay: 是否延迟升级。
        :type delay: str
        """
        
        

        self._databases_instance_infos = None
        self._delay = None
        self.discriminator = None

        self.databases_instance_infos = databases_instance_infos
        self.delay = delay

    @property
    def databases_instance_infos(self):
        r"""Gets the databases_instance_infos of this BatchUpgradeDatabasesRequestBody.

        要版本升级的批量实例。

        :return: The databases_instance_infos of this BatchUpgradeDatabasesRequestBody.
        :rtype: list[:class:`huaweicloudsdkgaussdb.v3.UpgradeDatabasesSingleInstance`]
        """
        return self._databases_instance_infos

    @databases_instance_infos.setter
    def databases_instance_infos(self, databases_instance_infos):
        r"""Sets the databases_instance_infos of this BatchUpgradeDatabasesRequestBody.

        要版本升级的批量实例。

        :param databases_instance_infos: The databases_instance_infos of this BatchUpgradeDatabasesRequestBody.
        :type databases_instance_infos: list[:class:`huaweicloudsdkgaussdb.v3.UpgradeDatabasesSingleInstance`]
        """
        self._databases_instance_infos = databases_instance_infos

    @property
    def delay(self):
        r"""Gets the delay of this BatchUpgradeDatabasesRequestBody.

        是否延迟升级。

        :return: The delay of this BatchUpgradeDatabasesRequestBody.
        :rtype: str
        """
        return self._delay

    @delay.setter
    def delay(self, delay):
        r"""Sets the delay of this BatchUpgradeDatabasesRequestBody.

        是否延迟升级。

        :param delay: The delay of this BatchUpgradeDatabasesRequestBody.
        :type delay: str
        """
        self._delay = delay

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, BatchUpgradeDatabasesRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
