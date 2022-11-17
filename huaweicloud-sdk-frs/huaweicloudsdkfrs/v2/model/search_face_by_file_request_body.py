# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SearchFaceByFileRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'image_file': 'file',
        'top_n': 'int',
        'threshold': 'float',
        'sort': 'str',
        'filter': 'str',
        'return_fields': 'str'
    }

    attribute_map = {
        'image_file': 'image_file',
        'top_n': 'top_n',
        'threshold': 'threshold',
        'sort': 'sort',
        'filter': 'filter',
        'return_fields': 'return_fields'
    }

    def __init__(self, image_file=None, top_n=None, threshold=None, sort=None, filter=None, return_fields=None):
        """SearchFaceByFileRequestBody

        The model defined in huaweicloud sdk

        :param image_file: 本地图片文件，图片不能超过8MB,建议小于1MB。上传文件时，请求格式为multipart。  必选，与image_url、image_base64、face_id四选一。
        :type image_file: :class:`huaweicloudsdkcore.http.formdata.FormFile`
        :param top_n: 返回查询到的最相似的N张人脸，N默认为10。
        :type top_n: int
        :param threshold: 人脸相似度阈值，低于这个阈值则不返回，取值范围0~1，一般情况下建议取值0.93，默认为0。
        :type threshold: float
        :param sort: [支持字段排序，参考[sort语法](https://support.huaweicloud.com/api-face/face_02_0013.html)。](tag:hc) [支持字段排序，参考[sort语法](https://support.huaweicloud.com/intl/zh-cn/api-face/face_02_0013.html)。](tag:hk)
        :type sort: str
        :param filter: [过滤条件，参考[filter语法](https://support.huaweicloud.com/api-face/face_02_0014.html)。](tag:hc) [过滤条件，参考[filter语法](https://support.huaweicloud.com/intl/zh-cn/api-face/face_02_0014.html)。](tag:hk)
        :type filter: str
        :param return_fields: 指定返回的自定义字段。
        :type return_fields: str
        """
        
        

        self._image_file = None
        self._top_n = None
        self._threshold = None
        self._sort = None
        self._filter = None
        self._return_fields = None
        self.discriminator = None

        self.image_file = image_file
        if top_n is not None:
            self.top_n = top_n
        if threshold is not None:
            self.threshold = threshold
        if sort is not None:
            self.sort = sort
        if filter is not None:
            self.filter = filter
        if return_fields is not None:
            self.return_fields = return_fields

    @property
    def image_file(self):
        """Gets the image_file of this SearchFaceByFileRequestBody.

        本地图片文件，图片不能超过8MB,建议小于1MB。上传文件时，请求格式为multipart。  必选，与image_url、image_base64、face_id四选一。

        :return: The image_file of this SearchFaceByFileRequestBody.
        :rtype: :class:`huaweicloudsdkcore.http.formdata.FormFile`
        """
        return self._image_file

    @image_file.setter
    def image_file(self, image_file):
        """Sets the image_file of this SearchFaceByFileRequestBody.

        本地图片文件，图片不能超过8MB,建议小于1MB。上传文件时，请求格式为multipart。  必选，与image_url、image_base64、face_id四选一。

        :param image_file: The image_file of this SearchFaceByFileRequestBody.
        :type image_file: :class:`huaweicloudsdkcore.http.formdata.FormFile`
        """
        self._image_file = image_file

    @property
    def top_n(self):
        """Gets the top_n of this SearchFaceByFileRequestBody.

        返回查询到的最相似的N张人脸，N默认为10。

        :return: The top_n of this SearchFaceByFileRequestBody.
        :rtype: int
        """
        return self._top_n

    @top_n.setter
    def top_n(self, top_n):
        """Sets the top_n of this SearchFaceByFileRequestBody.

        返回查询到的最相似的N张人脸，N默认为10。

        :param top_n: The top_n of this SearchFaceByFileRequestBody.
        :type top_n: int
        """
        self._top_n = top_n

    @property
    def threshold(self):
        """Gets the threshold of this SearchFaceByFileRequestBody.

        人脸相似度阈值，低于这个阈值则不返回，取值范围0~1，一般情况下建议取值0.93，默认为0。

        :return: The threshold of this SearchFaceByFileRequestBody.
        :rtype: float
        """
        return self._threshold

    @threshold.setter
    def threshold(self, threshold):
        """Sets the threshold of this SearchFaceByFileRequestBody.

        人脸相似度阈值，低于这个阈值则不返回，取值范围0~1，一般情况下建议取值0.93，默认为0。

        :param threshold: The threshold of this SearchFaceByFileRequestBody.
        :type threshold: float
        """
        self._threshold = threshold

    @property
    def sort(self):
        """Gets the sort of this SearchFaceByFileRequestBody.

        [支持字段排序，参考[sort语法](https://support.huaweicloud.com/api-face/face_02_0013.html)。](tag:hc) [支持字段排序，参考[sort语法](https://support.huaweicloud.com/intl/zh-cn/api-face/face_02_0013.html)。](tag:hk)

        :return: The sort of this SearchFaceByFileRequestBody.
        :rtype: str
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        """Sets the sort of this SearchFaceByFileRequestBody.

        [支持字段排序，参考[sort语法](https://support.huaweicloud.com/api-face/face_02_0013.html)。](tag:hc) [支持字段排序，参考[sort语法](https://support.huaweicloud.com/intl/zh-cn/api-face/face_02_0013.html)。](tag:hk)

        :param sort: The sort of this SearchFaceByFileRequestBody.
        :type sort: str
        """
        self._sort = sort

    @property
    def filter(self):
        """Gets the filter of this SearchFaceByFileRequestBody.

        [过滤条件，参考[filter语法](https://support.huaweicloud.com/api-face/face_02_0014.html)。](tag:hc) [过滤条件，参考[filter语法](https://support.huaweicloud.com/intl/zh-cn/api-face/face_02_0014.html)。](tag:hk)

        :return: The filter of this SearchFaceByFileRequestBody.
        :rtype: str
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this SearchFaceByFileRequestBody.

        [过滤条件，参考[filter语法](https://support.huaweicloud.com/api-face/face_02_0014.html)。](tag:hc) [过滤条件，参考[filter语法](https://support.huaweicloud.com/intl/zh-cn/api-face/face_02_0014.html)。](tag:hk)

        :param filter: The filter of this SearchFaceByFileRequestBody.
        :type filter: str
        """
        self._filter = filter

    @property
    def return_fields(self):
        """Gets the return_fields of this SearchFaceByFileRequestBody.

        指定返回的自定义字段。

        :return: The return_fields of this SearchFaceByFileRequestBody.
        :rtype: str
        """
        return self._return_fields

    @return_fields.setter
    def return_fields(self, return_fields):
        """Sets the return_fields of this SearchFaceByFileRequestBody.

        指定返回的自定义字段。

        :param return_fields: The return_fields of this SearchFaceByFileRequestBody.
        :type return_fields: str
        """
        self._return_fields = return_fields

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
        if not isinstance(other, SearchFaceByFileRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
