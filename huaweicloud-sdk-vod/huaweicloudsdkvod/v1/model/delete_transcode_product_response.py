# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteTranscodeProductResponse(SdkResponse):

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
        'status': 'str',
        'deleted_products': 'list[ProductGroupInfo]',
        'failed_products': 'list[ProductGroupDelFailInfo]'
    }

    attribute_map = {
        'asset_id': 'asset_id',
        'status': 'status',
        'deleted_products': 'deleted_products',
        'failed_products': 'failed_products'
    }

    def __init__(self, asset_id=None, status=None, deleted_products=None, failed_products=None):
        r"""DeleteTranscodeProductResponse

        The model defined in huaweicloud sdk

        :param asset_id: 媒资ID
        :type asset_id: str
        :param status: SUCCESS：成功 FAIL：失败 PARTIAL_SUCCESS：部分成功 
        :type status: str
        :param deleted_products: 删除成功的产物
        :type deleted_products: list[:class:`huaweicloudsdkvod.v1.ProductGroupInfo`]
        :param failed_products: 删除失败的产物
        :type failed_products: list[:class:`huaweicloudsdkvod.v1.ProductGroupDelFailInfo`]
        """
        
        super(DeleteTranscodeProductResponse, self).__init__()

        self._asset_id = None
        self._status = None
        self._deleted_products = None
        self._failed_products = None
        self.discriminator = None

        if asset_id is not None:
            self.asset_id = asset_id
        if status is not None:
            self.status = status
        if deleted_products is not None:
            self.deleted_products = deleted_products
        if failed_products is not None:
            self.failed_products = failed_products

    @property
    def asset_id(self):
        r"""Gets the asset_id of this DeleteTranscodeProductResponse.

        媒资ID

        :return: The asset_id of this DeleteTranscodeProductResponse.
        :rtype: str
        """
        return self._asset_id

    @asset_id.setter
    def asset_id(self, asset_id):
        r"""Sets the asset_id of this DeleteTranscodeProductResponse.

        媒资ID

        :param asset_id: The asset_id of this DeleteTranscodeProductResponse.
        :type asset_id: str
        """
        self._asset_id = asset_id

    @property
    def status(self):
        r"""Gets the status of this DeleteTranscodeProductResponse.

        SUCCESS：成功 FAIL：失败 PARTIAL_SUCCESS：部分成功 

        :return: The status of this DeleteTranscodeProductResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this DeleteTranscodeProductResponse.

        SUCCESS：成功 FAIL：失败 PARTIAL_SUCCESS：部分成功 

        :param status: The status of this DeleteTranscodeProductResponse.
        :type status: str
        """
        self._status = status

    @property
    def deleted_products(self):
        r"""Gets the deleted_products of this DeleteTranscodeProductResponse.

        删除成功的产物

        :return: The deleted_products of this DeleteTranscodeProductResponse.
        :rtype: list[:class:`huaweicloudsdkvod.v1.ProductGroupInfo`]
        """
        return self._deleted_products

    @deleted_products.setter
    def deleted_products(self, deleted_products):
        r"""Sets the deleted_products of this DeleteTranscodeProductResponse.

        删除成功的产物

        :param deleted_products: The deleted_products of this DeleteTranscodeProductResponse.
        :type deleted_products: list[:class:`huaweicloudsdkvod.v1.ProductGroupInfo`]
        """
        self._deleted_products = deleted_products

    @property
    def failed_products(self):
        r"""Gets the failed_products of this DeleteTranscodeProductResponse.

        删除失败的产物

        :return: The failed_products of this DeleteTranscodeProductResponse.
        :rtype: list[:class:`huaweicloudsdkvod.v1.ProductGroupDelFailInfo`]
        """
        return self._failed_products

    @failed_products.setter
    def failed_products(self, failed_products):
        r"""Sets the failed_products of this DeleteTranscodeProductResponse.

        删除失败的产物

        :param failed_products: The failed_products of this DeleteTranscodeProductResponse.
        :type failed_products: list[:class:`huaweicloudsdkvod.v1.ProductGroupDelFailInfo`]
        """
        self._failed_products = failed_products

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
        if not isinstance(other, DeleteTranscodeProductResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
