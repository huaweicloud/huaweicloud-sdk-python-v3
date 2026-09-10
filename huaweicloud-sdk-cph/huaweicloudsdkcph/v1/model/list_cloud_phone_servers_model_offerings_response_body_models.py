# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCloudPhoneServersModelOfferingsResponseBodyModels:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'available_zone': 'str',
        'model_name': 'str',
        'sell_status': 'str'
    }

    attribute_map = {
        'available_zone': 'available_zone',
        'model_name': 'model_name',
        'sell_status': 'sell_status'
    }

    def __init__(self, available_zone=None, model_name=None, sell_status=None):
        r"""ListCloudPhoneServersModelOfferingsResponseBodyModels

        The model defined in huaweicloud sdk

        :param available_zone: 可用区
        :type available_zone: str
        :param model_name: 云手机服务器规格名
        :type model_name: str
        :param sell_status: 云手机服务器规格的售卖状态。  - sellout：售罄  - available：可用
        :type sell_status: str
        """
        
        

        self._available_zone = None
        self._model_name = None
        self._sell_status = None
        self.discriminator = None

        if available_zone is not None:
            self.available_zone = available_zone
        if model_name is not None:
            self.model_name = model_name
        if sell_status is not None:
            self.sell_status = sell_status

    @property
    def available_zone(self):
        r"""Gets the available_zone of this ListCloudPhoneServersModelOfferingsResponseBodyModels.

        可用区

        :return: The available_zone of this ListCloudPhoneServersModelOfferingsResponseBodyModels.
        :rtype: str
        """
        return self._available_zone

    @available_zone.setter
    def available_zone(self, available_zone):
        r"""Sets the available_zone of this ListCloudPhoneServersModelOfferingsResponseBodyModels.

        可用区

        :param available_zone: The available_zone of this ListCloudPhoneServersModelOfferingsResponseBodyModels.
        :type available_zone: str
        """
        self._available_zone = available_zone

    @property
    def model_name(self):
        r"""Gets the model_name of this ListCloudPhoneServersModelOfferingsResponseBodyModels.

        云手机服务器规格名

        :return: The model_name of this ListCloudPhoneServersModelOfferingsResponseBodyModels.
        :rtype: str
        """
        return self._model_name

    @model_name.setter
    def model_name(self, model_name):
        r"""Sets the model_name of this ListCloudPhoneServersModelOfferingsResponseBodyModels.

        云手机服务器规格名

        :param model_name: The model_name of this ListCloudPhoneServersModelOfferingsResponseBodyModels.
        :type model_name: str
        """
        self._model_name = model_name

    @property
    def sell_status(self):
        r"""Gets the sell_status of this ListCloudPhoneServersModelOfferingsResponseBodyModels.

        云手机服务器规格的售卖状态。  - sellout：售罄  - available：可用

        :return: The sell_status of this ListCloudPhoneServersModelOfferingsResponseBodyModels.
        :rtype: str
        """
        return self._sell_status

    @sell_status.setter
    def sell_status(self, sell_status):
        r"""Sets the sell_status of this ListCloudPhoneServersModelOfferingsResponseBodyModels.

        云手机服务器规格的售卖状态。  - sellout：售罄  - available：可用

        :param sell_status: The sell_status of this ListCloudPhoneServersModelOfferingsResponseBodyModels.
        :type sell_status: str
        """
        self._sell_status = sell_status

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
        if not isinstance(other, ListCloudPhoneServersModelOfferingsResponseBodyModels):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
