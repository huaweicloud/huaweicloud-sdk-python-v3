# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BindAssetResourceReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'asset_id': 'str',
        'business_type': 'str'
    }

    attribute_map = {
        'asset_id': 'asset_id',
        'business_type': 'business_type'
    }

    def __init__(self, asset_id=None, business_type=None):
        r"""BindAssetResourceReq

        The model defined in huaweicloud sdk

        :param asset_id: 资产id。
        :type asset_id: str
        :param business_type: 业务类型。
        :type business_type: str
        """
        
        

        self._asset_id = None
        self._business_type = None
        self.discriminator = None

        if asset_id is not None:
            self.asset_id = asset_id
        if business_type is not None:
            self.business_type = business_type

    @property
    def asset_id(self):
        r"""Gets the asset_id of this BindAssetResourceReq.

        资产id。

        :return: The asset_id of this BindAssetResourceReq.
        :rtype: str
        """
        return self._asset_id

    @asset_id.setter
    def asset_id(self, asset_id):
        r"""Sets the asset_id of this BindAssetResourceReq.

        资产id。

        :param asset_id: The asset_id of this BindAssetResourceReq.
        :type asset_id: str
        """
        self._asset_id = asset_id

    @property
    def business_type(self):
        r"""Gets the business_type of this BindAssetResourceReq.

        业务类型。

        :return: The business_type of this BindAssetResourceReq.
        :rtype: str
        """
        return self._business_type

    @business_type.setter
    def business_type(self, business_type):
        r"""Sets the business_type of this BindAssetResourceReq.

        业务类型。

        :param business_type: The business_type of this BindAssetResourceReq.
        :type business_type: str
        """
        self._business_type = business_type

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
        if not isinstance(other, BindAssetResourceReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
