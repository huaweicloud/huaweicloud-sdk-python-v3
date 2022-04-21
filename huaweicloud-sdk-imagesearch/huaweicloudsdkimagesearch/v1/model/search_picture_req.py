# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SearchPictureReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'file': 'str',
        'path': 'str',
        'limit': 'int',
        'offset': 'int',
        'tags': 'object',
        'is_crop': 'bool',
        'box': 'SearchBoxDetail'
    }

    attribute_map = {
        'file': 'file',
        'path': 'path',
        'limit': 'limit',
        'offset': 'offset',
        'tags': 'tags',
        'is_crop': 'is_crop',
        'box': 'box'
    }

    def __init__(self, file=None, path=None, limit=None, offset=None, tags=None, is_crop=None, box=None):
        """SearchPictureReq

        The model defined in huaweicloud sdk

        :param file: 图片文件Base64编码字符串，仅支持JPEG/JPG/PNG/BMP格式，图片最小边不小于100px，最大边不超过2048px。该参数与path二选一，如果两个参数都存在，则以file为主。 
        :type file: str
        :param path: 图片的URL路径，图片库中的图片索引ID。该参数与file二选一，如果两个参数都存在，则以file为主。 
        :type path: str
        :param limit: 返回被检索图像的数量，取值为1~100的整数，默认为10。
        :type limit: int
        :param offset: 偏移量，指定搜索结果返回起始位置，取值为大于或等于0的整数，默认为0。
        :type offset: int
        :param tags: 图片自定义标签，最多不超过10个，格式为key：value对。 标签名（key）添加方式：   - 登录管理控制台，单击“创建实例”，自定义标签名。   - 登录管理控制台，在“实例管理”页签，单击实例名称，进入“基础信息”页添加自定义标签。 使用图片标签搜索时该参数必选。
        :type tags: object
        :param is_crop: 是否用图片中指定区域（参数box）进行搜索。默认为false，该参数目前仅对某些特定模型有效，其他模型暂不支持目标检测。 - true：用图片中指定区域（参数box）进行搜索。 - false：用全图进行搜索。
        :type is_crop: bool
        :param box: 
        :type box: :class:`huaweicloudsdkimagesearch.v1.SearchBoxDetail`
        """
        
        

        self._file = None
        self._path = None
        self._limit = None
        self._offset = None
        self._tags = None
        self._is_crop = None
        self._box = None
        self.discriminator = None

        if file is not None:
            self.file = file
        if path is not None:
            self.path = path
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if tags is not None:
            self.tags = tags
        if is_crop is not None:
            self.is_crop = is_crop
        if box is not None:
            self.box = box

    @property
    def file(self):
        """Gets the file of this SearchPictureReq.

        图片文件Base64编码字符串，仅支持JPEG/JPG/PNG/BMP格式，图片最小边不小于100px，最大边不超过2048px。该参数与path二选一，如果两个参数都存在，则以file为主。 

        :return: The file of this SearchPictureReq.
        :rtype: str
        """
        return self._file

    @file.setter
    def file(self, file):
        """Sets the file of this SearchPictureReq.

        图片文件Base64编码字符串，仅支持JPEG/JPG/PNG/BMP格式，图片最小边不小于100px，最大边不超过2048px。该参数与path二选一，如果两个参数都存在，则以file为主。 

        :param file: The file of this SearchPictureReq.
        :type file: str
        """
        self._file = file

    @property
    def path(self):
        """Gets the path of this SearchPictureReq.

        图片的URL路径，图片库中的图片索引ID。该参数与file二选一，如果两个参数都存在，则以file为主。 

        :return: The path of this SearchPictureReq.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this SearchPictureReq.

        图片的URL路径，图片库中的图片索引ID。该参数与file二选一，如果两个参数都存在，则以file为主。 

        :param path: The path of this SearchPictureReq.
        :type path: str
        """
        self._path = path

    @property
    def limit(self):
        """Gets the limit of this SearchPictureReq.

        返回被检索图像的数量，取值为1~100的整数，默认为10。

        :return: The limit of this SearchPictureReq.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this SearchPictureReq.

        返回被检索图像的数量，取值为1~100的整数，默认为10。

        :param limit: The limit of this SearchPictureReq.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this SearchPictureReq.

        偏移量，指定搜索结果返回起始位置，取值为大于或等于0的整数，默认为0。

        :return: The offset of this SearchPictureReq.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this SearchPictureReq.

        偏移量，指定搜索结果返回起始位置，取值为大于或等于0的整数，默认为0。

        :param offset: The offset of this SearchPictureReq.
        :type offset: int
        """
        self._offset = offset

    @property
    def tags(self):
        """Gets the tags of this SearchPictureReq.

        图片自定义标签，最多不超过10个，格式为key：value对。 标签名（key）添加方式：   - 登录管理控制台，单击“创建实例”，自定义标签名。   - 登录管理控制台，在“实例管理”页签，单击实例名称，进入“基础信息”页添加自定义标签。 使用图片标签搜索时该参数必选。

        :return: The tags of this SearchPictureReq.
        :rtype: object
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this SearchPictureReq.

        图片自定义标签，最多不超过10个，格式为key：value对。 标签名（key）添加方式：   - 登录管理控制台，单击“创建实例”，自定义标签名。   - 登录管理控制台，在“实例管理”页签，单击实例名称，进入“基础信息”页添加自定义标签。 使用图片标签搜索时该参数必选。

        :param tags: The tags of this SearchPictureReq.
        :type tags: object
        """
        self._tags = tags

    @property
    def is_crop(self):
        """Gets the is_crop of this SearchPictureReq.

        是否用图片中指定区域（参数box）进行搜索。默认为false，该参数目前仅对某些特定模型有效，其他模型暂不支持目标检测。 - true：用图片中指定区域（参数box）进行搜索。 - false：用全图进行搜索。

        :return: The is_crop of this SearchPictureReq.
        :rtype: bool
        """
        return self._is_crop

    @is_crop.setter
    def is_crop(self, is_crop):
        """Sets the is_crop of this SearchPictureReq.

        是否用图片中指定区域（参数box）进行搜索。默认为false，该参数目前仅对某些特定模型有效，其他模型暂不支持目标检测。 - true：用图片中指定区域（参数box）进行搜索。 - false：用全图进行搜索。

        :param is_crop: The is_crop of this SearchPictureReq.
        :type is_crop: bool
        """
        self._is_crop = is_crop

    @property
    def box(self):
        """Gets the box of this SearchPictureReq.


        :return: The box of this SearchPictureReq.
        :rtype: :class:`huaweicloudsdkimagesearch.v1.SearchBoxDetail`
        """
        return self._box

    @box.setter
    def box(self, box):
        """Sets the box of this SearchPictureReq.


        :param box: The box of this SearchPictureReq.
        :type box: :class:`huaweicloudsdkimagesearch.v1.SearchBoxDetail`
        """
        self._box = box

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
        if not isinstance(other, SearchPictureReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
