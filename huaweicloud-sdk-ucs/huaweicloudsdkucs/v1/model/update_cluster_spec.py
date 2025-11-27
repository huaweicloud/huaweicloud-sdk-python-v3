# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateClusterSpec:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'country': 'str',
        'city': 'str',
        'worker_config': 'WorkerConfig'
    }

    attribute_map = {
        'country': 'country',
        'city': 'city',
        'worker_config': 'workerConfig'
    }

    def __init__(self, country=None, city=None, worker_config=None):
        r"""UpdateClusterSpec

        The model defined in huaweicloud sdk

        :param country: 集群所在国家信息
        :type country: str
        :param city: 集群所在城市信息
        :type city: str
        :param worker_config: 
        :type worker_config: :class:`huaweicloudsdkucs.v1.WorkerConfig`
        """
        
        

        self._country = None
        self._city = None
        self._worker_config = None
        self.discriminator = None

        if country is not None:
            self.country = country
        if city is not None:
            self.city = city
        if worker_config is not None:
            self.worker_config = worker_config

    @property
    def country(self):
        r"""Gets the country of this UpdateClusterSpec.

        集群所在国家信息

        :return: The country of this UpdateClusterSpec.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        r"""Sets the country of this UpdateClusterSpec.

        集群所在国家信息

        :param country: The country of this UpdateClusterSpec.
        :type country: str
        """
        self._country = country

    @property
    def city(self):
        r"""Gets the city of this UpdateClusterSpec.

        集群所在城市信息

        :return: The city of this UpdateClusterSpec.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        r"""Sets the city of this UpdateClusterSpec.

        集群所在城市信息

        :param city: The city of this UpdateClusterSpec.
        :type city: str
        """
        self._city = city

    @property
    def worker_config(self):
        r"""Gets the worker_config of this UpdateClusterSpec.

        :return: The worker_config of this UpdateClusterSpec.
        :rtype: :class:`huaweicloudsdkucs.v1.WorkerConfig`
        """
        return self._worker_config

    @worker_config.setter
    def worker_config(self, worker_config):
        r"""Sets the worker_config of this UpdateClusterSpec.

        :param worker_config: The worker_config of this UpdateClusterSpec.
        :type worker_config: :class:`huaweicloudsdkucs.v1.WorkerConfig`
        """
        self._worker_config = worker_config

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
        if not isinstance(other, UpdateClusterSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
