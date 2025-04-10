# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateAssetNewRequest:

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
        'body': 'AssetModRequest'
    }

    attribute_map = {
        'asset_id': 'asset_id',
        'body': 'body'
    }

    def __init__(self, asset_id=None, body=None):
        r"""UpdateAssetNewRequest

        The model defined in huaweicloud sdk

        :param asset_id: 资产ID
        :type asset_id: str
        :param body: Body of the UpdateAssetNewRequest
        :type body: :class:`huaweicloudsdkiotanalytics.v1.AssetModRequest`
        """
        
        

        self._asset_id = None
        self._body = None
        self.discriminator = None

        self.asset_id = asset_id
        if body is not None:
            self.body = body

    @property
    def asset_id(self):
        r"""Gets the asset_id of this UpdateAssetNewRequest.

        资产ID

        :return: The asset_id of this UpdateAssetNewRequest.
        :rtype: str
        """
        return self._asset_id

    @asset_id.setter
    def asset_id(self, asset_id):
        r"""Sets the asset_id of this UpdateAssetNewRequest.

        资产ID

        :param asset_id: The asset_id of this UpdateAssetNewRequest.
        :type asset_id: str
        """
        self._asset_id = asset_id

    @property
    def body(self):
        r"""Gets the body of this UpdateAssetNewRequest.

        :return: The body of this UpdateAssetNewRequest.
        :rtype: :class:`huaweicloudsdkiotanalytics.v1.AssetModRequest`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateAssetNewRequest.

        :param body: The body of this UpdateAssetNewRequest.
        :type body: :class:`huaweicloudsdkiotanalytics.v1.AssetModRequest`
        """
        self._body = body

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
        if not isinstance(other, UpdateAssetNewRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
