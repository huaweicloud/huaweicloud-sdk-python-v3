# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FaceSearchUrlReq:


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
        'image_url': 'str',
        'return_fields': 'list[str]',
        'threshold': 'float',
        'sort': 'list[dict(str, str)]'
    }

    attribute_map = {
        'filter': 'filter',
        'top_n': 'top_n',
        'image_url': 'image_url',
        'return_fields': 'return_fields',
        'threshold': 'threshold',
        'sort': 'sort'
    }

    def __init__(self, filter=None, top_n=None, image_url=None, return_fields=None, threshold=None, sort=None):
        """FaceSearchUrlReq - a model defined in huaweicloud sdk"""
        
        

        self._filter = None
        self._top_n = None
        self._image_url = None
        self._return_fields = None
        self._threshold = None
        self._sort = None
        self.discriminator = None

        if filter is not None:
            self.filter = filter
        if top_n is not None:
            self.top_n = top_n
        self.image_url = image_url
        if return_fields is not None:
            self.return_fields = return_fields
        if threshold is not None:
            self.threshold = threshold
        if sort is not None:
            self.sort = sort

    @property
    def filter(self):
        """Gets the filter of this FaceSearchUrlReq.

        过滤条件，参考[filter语法](zh-cn_topic_0130807048.xml)。

        :return: The filter of this FaceSearchUrlReq.
        :rtype: str
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this FaceSearchUrlReq.

        过滤条件，参考[filter语法](zh-cn_topic_0130807048.xml)。

        :param filter: The filter of this FaceSearchUrlReq.
        :type: str
        """
        self._filter = filter

    @property
    def top_n(self):
        """Gets the top_n of this FaceSearchUrlReq.

        返回查询到的最相似的N张人脸，N默认为10。

        :return: The top_n of this FaceSearchUrlReq.
        :rtype: int
        """
        return self._top_n

    @top_n.setter
    def top_n(self, top_n):
        """Sets the top_n of this FaceSearchUrlReq.

        返回查询到的最相似的N张人脸，N默认为10。

        :param top_n: The top_n of this FaceSearchUrlReq.
        :type: int
        """
        self._top_n = top_n

    @property
    def image_url(self):
        """Gets the image_url of this FaceSearchUrlReq.

        图片的URL路径，目前仅支持华为云上OBS的URL，且人脸识别服务有权限读取该OBS桶的数据。 开通读取权限的操作请参见[服务授权](zh-cn_topic_0107696818.xml)。

        :return: The image_url of this FaceSearchUrlReq.
        :rtype: str
        """
        return self._image_url

    @image_url.setter
    def image_url(self, image_url):
        """Sets the image_url of this FaceSearchUrlReq.

        图片的URL路径，目前仅支持华为云上OBS的URL，且人脸识别服务有权限读取该OBS桶的数据。 开通读取权限的操作请参见[服务授权](zh-cn_topic_0107696818.xml)。

        :param image_url: The image_url of this FaceSearchUrlReq.
        :type: str
        """
        self._image_url = image_url

    @property
    def return_fields(self):
        """Gets the return_fields of this FaceSearchUrlReq.

        指定返回的自定义字段。

        :return: The return_fields of this FaceSearchUrlReq.
        :rtype: list[str]
        """
        return self._return_fields

    @return_fields.setter
    def return_fields(self, return_fields):
        """Sets the return_fields of this FaceSearchUrlReq.

        指定返回的自定义字段。

        :param return_fields: The return_fields of this FaceSearchUrlReq.
        :type: list[str]
        """
        self._return_fields = return_fields

    @property
    def threshold(self):
        """Gets the threshold of this FaceSearchUrlReq.

        人脸相似度阈值，低于这个阈值则不返回，取值范围0~1，一般情况下建议取值0.93，默认为0。

        :return: The threshold of this FaceSearchUrlReq.
        :rtype: float
        """
        return self._threshold

    @threshold.setter
    def threshold(self, threshold):
        """Sets the threshold of this FaceSearchUrlReq.

        人脸相似度阈值，低于这个阈值则不返回，取值范围0~1，一般情况下建议取值0.93，默认为0。

        :param threshold: The threshold of this FaceSearchUrlReq.
        :type: float
        """
        self._threshold = threshold

    @property
    def sort(self):
        """Gets the sort of this FaceSearchUrlReq.

        支持字段排序，参考[sort语法](zh-cn_topic_0130807047.xml)。

        :return: The sort of this FaceSearchUrlReq.
        :rtype: list[dict(str, str)]
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        """Sets the sort of this FaceSearchUrlReq.

        支持字段排序，参考[sort语法](zh-cn_topic_0130807047.xml)。

        :param sort: The sort of this FaceSearchUrlReq.
        :type: list[dict(str, str)]
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
        if not isinstance(other, FaceSearchUrlReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
