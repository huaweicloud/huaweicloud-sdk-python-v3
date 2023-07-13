# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FaceSearchBase64Req:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'filter': 'str',
        'top_n': 'int',
        'image_base64': 'str',
        'return_fields': 'list[str]',
        'threshold': 'float',
        'sort': 'list[dict(str, str)]'
    }

    attribute_map = {
        'filter': 'filter',
        'top_n': 'top_n',
        'image_base64': 'image_base64',
        'return_fields': 'return_fields',
        'threshold': 'threshold',
        'sort': 'sort'
    }

    def __init__(self, filter=None, top_n=None, image_base64=None, return_fields=None, threshold=None, sort=None):
        """FaceSearchBase64Req

        The model defined in huaweicloud sdk

        :param filter: [过滤条件，参考[filter语法](https://support.huaweicloud.com/api-face/face_02_0014.html)。](tag:hc) [过滤条件，参考[filter语法](https://support.huaweicloud.com/intl/zh-cn/api-face/face_02_0014.html)。](tag:hk)
        :type filter: str
        :param top_n: 返回查询到的最相似的N张人脸，N默认为10。
        :type top_n: int
        :param image_base64: 图像数据，Base64编码，要求： • Base64编码后大小不超过8MB，建议小于MB。 • 图片为JPG/JPEG/BMP/PNG格式。
        :type image_base64: str
        :param return_fields: 指定返回的自定义字段。
        :type return_fields: list[str]
        :param threshold: 人脸相似度阈值，低于这个阈值则不返回，取值范围0~1，一般情况下建议取值0.93，默认为0。
        :type threshold: float
        :param sort: [支持字段排序，参考[sort语法](https://support.huaweicloud.com/api-face/face_02_0013.html)。](tag:hc) [支持字段排序，参考[sort语法](https://support.huaweicloud.com/intl/zh-cn/api-face/face_02_0013.html)。](tag:hk)
        :type sort: list[dict(str, str)]
        """
        
        

        self._filter = None
        self._top_n = None
        self._image_base64 = None
        self._return_fields = None
        self._threshold = None
        self._sort = None
        self.discriminator = None

        if filter is not None:
            self.filter = filter
        if top_n is not None:
            self.top_n = top_n
        self.image_base64 = image_base64
        if return_fields is not None:
            self.return_fields = return_fields
        if threshold is not None:
            self.threshold = threshold
        if sort is not None:
            self.sort = sort

    @property
    def filter(self):
        """Gets the filter of this FaceSearchBase64Req.

        [过滤条件，参考[filter语法](https://support.huaweicloud.com/api-face/face_02_0014.html)。](tag:hc) [过滤条件，参考[filter语法](https://support.huaweicloud.com/intl/zh-cn/api-face/face_02_0014.html)。](tag:hk)

        :return: The filter of this FaceSearchBase64Req.
        :rtype: str
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this FaceSearchBase64Req.

        [过滤条件，参考[filter语法](https://support.huaweicloud.com/api-face/face_02_0014.html)。](tag:hc) [过滤条件，参考[filter语法](https://support.huaweicloud.com/intl/zh-cn/api-face/face_02_0014.html)。](tag:hk)

        :param filter: The filter of this FaceSearchBase64Req.
        :type filter: str
        """
        self._filter = filter

    @property
    def top_n(self):
        """Gets the top_n of this FaceSearchBase64Req.

        返回查询到的最相似的N张人脸，N默认为10。

        :return: The top_n of this FaceSearchBase64Req.
        :rtype: int
        """
        return self._top_n

    @top_n.setter
    def top_n(self, top_n):
        """Sets the top_n of this FaceSearchBase64Req.

        返回查询到的最相似的N张人脸，N默认为10。

        :param top_n: The top_n of this FaceSearchBase64Req.
        :type top_n: int
        """
        self._top_n = top_n

    @property
    def image_base64(self):
        """Gets the image_base64 of this FaceSearchBase64Req.

        图像数据，Base64编码，要求： • Base64编码后大小不超过8MB，建议小于MB。 • 图片为JPG/JPEG/BMP/PNG格式。

        :return: The image_base64 of this FaceSearchBase64Req.
        :rtype: str
        """
        return self._image_base64

    @image_base64.setter
    def image_base64(self, image_base64):
        """Sets the image_base64 of this FaceSearchBase64Req.

        图像数据，Base64编码，要求： • Base64编码后大小不超过8MB，建议小于MB。 • 图片为JPG/JPEG/BMP/PNG格式。

        :param image_base64: The image_base64 of this FaceSearchBase64Req.
        :type image_base64: str
        """
        self._image_base64 = image_base64

    @property
    def return_fields(self):
        """Gets the return_fields of this FaceSearchBase64Req.

        指定返回的自定义字段。

        :return: The return_fields of this FaceSearchBase64Req.
        :rtype: list[str]
        """
        return self._return_fields

    @return_fields.setter
    def return_fields(self, return_fields):
        """Sets the return_fields of this FaceSearchBase64Req.

        指定返回的自定义字段。

        :param return_fields: The return_fields of this FaceSearchBase64Req.
        :type return_fields: list[str]
        """
        self._return_fields = return_fields

    @property
    def threshold(self):
        """Gets the threshold of this FaceSearchBase64Req.

        人脸相似度阈值，低于这个阈值则不返回，取值范围0~1，一般情况下建议取值0.93，默认为0。

        :return: The threshold of this FaceSearchBase64Req.
        :rtype: float
        """
        return self._threshold

    @threshold.setter
    def threshold(self, threshold):
        """Sets the threshold of this FaceSearchBase64Req.

        人脸相似度阈值，低于这个阈值则不返回，取值范围0~1，一般情况下建议取值0.93，默认为0。

        :param threshold: The threshold of this FaceSearchBase64Req.
        :type threshold: float
        """
        self._threshold = threshold

    @property
    def sort(self):
        """Gets the sort of this FaceSearchBase64Req.

        [支持字段排序，参考[sort语法](https://support.huaweicloud.com/api-face/face_02_0013.html)。](tag:hc) [支持字段排序，参考[sort语法](https://support.huaweicloud.com/intl/zh-cn/api-face/face_02_0013.html)。](tag:hk)

        :return: The sort of this FaceSearchBase64Req.
        :rtype: list[dict(str, str)]
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        """Sets the sort of this FaceSearchBase64Req.

        [支持字段排序，参考[sort语法](https://support.huaweicloud.com/api-face/face_02_0013.html)。](tag:hc) [支持字段排序，参考[sort语法](https://support.huaweicloud.com/intl/zh-cn/api-face/face_02_0013.html)。](tag:hk)

        :param sort: The sort of this FaceSearchBase64Req.
        :type sort: list[dict(str, str)]
        """
        self._sort = sort

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
        if not isinstance(other, FaceSearchBase64Req):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
