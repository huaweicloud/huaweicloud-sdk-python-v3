# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListImagesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'image_infos': 'list[ListImagesView]',
        'total': 'int',
        'request_id': 'str'
    }

    attribute_map = {
        'image_infos': 'image_infos',
        'total': 'total',
        'request_id': 'request_id'
    }

    def __init__(self, image_infos=None, total=None, request_id=None):
        r"""ListImagesResponse

        The model defined in huaweicloud sdk

        :param image_infos: 镜像详情
        :type image_infos: list[:class:`huaweicloudsdkcph.v1.ListImagesView`]
        :param total: 总条数
        :type total: int
        :param request_id: 请求的唯一标识ID。
        :type request_id: str
        """
        
        super(ListImagesResponse, self).__init__()

        self._image_infos = None
        self._total = None
        self._request_id = None
        self.discriminator = None

        if image_infos is not None:
            self.image_infos = image_infos
        if total is not None:
            self.total = total
        if request_id is not None:
            self.request_id = request_id

    @property
    def image_infos(self):
        r"""Gets the image_infos of this ListImagesResponse.

        镜像详情

        :return: The image_infos of this ListImagesResponse.
        :rtype: list[:class:`huaweicloudsdkcph.v1.ListImagesView`]
        """
        return self._image_infos

    @image_infos.setter
    def image_infos(self, image_infos):
        r"""Sets the image_infos of this ListImagesResponse.

        镜像详情

        :param image_infos: The image_infos of this ListImagesResponse.
        :type image_infos: list[:class:`huaweicloudsdkcph.v1.ListImagesView`]
        """
        self._image_infos = image_infos

    @property
    def total(self):
        r"""Gets the total of this ListImagesResponse.

        总条数

        :return: The total of this ListImagesResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListImagesResponse.

        总条数

        :param total: The total of this ListImagesResponse.
        :type total: int
        """
        self._total = total

    @property
    def request_id(self):
        r"""Gets the request_id of this ListImagesResponse.

        请求的唯一标识ID。

        :return: The request_id of this ListImagesResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        r"""Sets the request_id of this ListImagesResponse.

        请求的唯一标识ID。

        :param request_id: The request_id of this ListImagesResponse.
        :type request_id: str
        """
        self._request_id = request_id

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
        if not isinstance(other, ListImagesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
