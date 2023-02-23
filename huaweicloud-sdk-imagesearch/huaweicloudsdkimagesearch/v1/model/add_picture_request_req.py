# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddPictureRequestReq:

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
        'tags': 'object'
    }

    attribute_map = {
        'file': 'file',
        'path': 'path',
        'tags': 'tags'
    }

    def __init__(self, file=None, path=None, tags=None):
        """AddPictureRequestReq

        The model defined in huaweicloud sdk

        :param file: 图片文件Base64编码字符串，仅支持JPEG/JPG/PNG/BMP格式，图片最小边不小于100px，最大边不超过2048px。
        :type file: str
        :param path: 图片的URL路径，作为图片库中索引图片的ID，是必选参数。  &gt; - 当file字段不为空时，图片从file获取，path作为图片索引ID使用；当file字段不存在或者为空时，图片需要通过下载获取，此时path作为下载图片的地址（当前仅支持从华为云图像搜索服务所在区域的OBS下载图片），同时，path也作为图片索引ID。 
        :type path: str
        :param tags: 图片自定义标签。格式为key：value对，所有图片的key总数最多不超过10个，但是每个key对应的value不限制个数，例如：key为动物，对应的value可以是猫、狗、鸟等多个。  标签名（key）添加方式：   - 登录管理控制台，单击“创建实例”，自定义标签名。    - 登录管理控制台，在“实例管理”页签，单击实例名称，进入“基础信息”页添加自定义标签。 
        :type tags: object
        """
        
        

        self._file = None
        self._path = None
        self._tags = None
        self.discriminator = None

        if file is not None:
            self.file = file
        self.path = path
        if tags is not None:
            self.tags = tags

    @property
    def file(self):
        """Gets the file of this AddPictureRequestReq.

        图片文件Base64编码字符串，仅支持JPEG/JPG/PNG/BMP格式，图片最小边不小于100px，最大边不超过2048px。

        :return: The file of this AddPictureRequestReq.
        :rtype: str
        """
        return self._file

    @file.setter
    def file(self, file):
        """Sets the file of this AddPictureRequestReq.

        图片文件Base64编码字符串，仅支持JPEG/JPG/PNG/BMP格式，图片最小边不小于100px，最大边不超过2048px。

        :param file: The file of this AddPictureRequestReq.
        :type file: str
        """
        self._file = file

    @property
    def path(self):
        """Gets the path of this AddPictureRequestReq.

        图片的URL路径，作为图片库中索引图片的ID，是必选参数。  > - 当file字段不为空时，图片从file获取，path作为图片索引ID使用；当file字段不存在或者为空时，图片需要通过下载获取，此时path作为下载图片的地址（当前仅支持从华为云图像搜索服务所在区域的OBS下载图片），同时，path也作为图片索引ID。 

        :return: The path of this AddPictureRequestReq.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this AddPictureRequestReq.

        图片的URL路径，作为图片库中索引图片的ID，是必选参数。  > - 当file字段不为空时，图片从file获取，path作为图片索引ID使用；当file字段不存在或者为空时，图片需要通过下载获取，此时path作为下载图片的地址（当前仅支持从华为云图像搜索服务所在区域的OBS下载图片），同时，path也作为图片索引ID。 

        :param path: The path of this AddPictureRequestReq.
        :type path: str
        """
        self._path = path

    @property
    def tags(self):
        """Gets the tags of this AddPictureRequestReq.

        图片自定义标签。格式为key：value对，所有图片的key总数最多不超过10个，但是每个key对应的value不限制个数，例如：key为动物，对应的value可以是猫、狗、鸟等多个。  标签名（key）添加方式：   - 登录管理控制台，单击“创建实例”，自定义标签名。    - 登录管理控制台，在“实例管理”页签，单击实例名称，进入“基础信息”页添加自定义标签。 

        :return: The tags of this AddPictureRequestReq.
        :rtype: object
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this AddPictureRequestReq.

        图片自定义标签。格式为key：value对，所有图片的key总数最多不超过10个，但是每个key对应的value不限制个数，例如：key为动物，对应的value可以是猫、狗、鸟等多个。  标签名（key）添加方式：   - 登录管理控制台，单击“创建实例”，自定义标签名。    - 登录管理控制台，在“实例管理”页签，单击实例名称，进入“基础信息”页添加自定义标签。 

        :param tags: The tags of this AddPictureRequestReq.
        :type tags: object
        """
        self._tags = tags

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
        if not isinstance(other, AddPictureRequestReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
