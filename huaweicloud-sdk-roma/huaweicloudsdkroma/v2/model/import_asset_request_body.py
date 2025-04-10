# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImportAssetRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'import_asset_request_body': 'file'
    }

    attribute_map = {
        'import_asset_request_body': 'ImportAssetRequestBody'
    }

    def __init__(self, import_asset_request_body=None):
        r"""ImportAssetRequestBody

        The model defined in huaweicloud sdk

        :param import_asset_request_body: 资产压缩文件
        :type import_asset_request_body: :class:`huaweicloudsdkcore.http.formdata.FormFile`
        """
        
        

        self._import_asset_request_body = None
        self.discriminator = None

        self.import_asset_request_body = import_asset_request_body

    @property
    def import_asset_request_body(self):
        r"""Gets the import_asset_request_body of this ImportAssetRequestBody.

        资产压缩文件

        :return: The import_asset_request_body of this ImportAssetRequestBody.
        :rtype: :class:`huaweicloudsdkcore.http.formdata.FormFile`
        """
        return self._import_asset_request_body

    @import_asset_request_body.setter
    def import_asset_request_body(self, import_asset_request_body):
        r"""Sets the import_asset_request_body of this ImportAssetRequestBody.

        资产压缩文件

        :param import_asset_request_body: The import_asset_request_body of this ImportAssetRequestBody.
        :type import_asset_request_body: :class:`huaweicloudsdkcore.http.formdata.FormFile`
        """
        self._import_asset_request_body = import_asset_request_body

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
        if not isinstance(other, ImportAssetRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
