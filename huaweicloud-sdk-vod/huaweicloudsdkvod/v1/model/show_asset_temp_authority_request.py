# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAssetTempAuthorityRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'http_verb': 'str',
        'bucket': 'str',
        'object_key': 'str',
        'content_type': 'str',
        'content_md5': 'str',
        'upload_id': 'str',
        'part_number': 'int'
    }

    attribute_map = {
        'http_verb': 'http_verb',
        'bucket': 'bucket',
        'object_key': 'object_key',
        'content_type': 'content_type',
        'content_md5': 'content_md5',
        'upload_id': 'upload_id',
        'part_number': 'part_number'
    }

    def __init__(self, http_verb=None, bucket=None, object_key=None, content_type=None, content_md5=None, upload_id=None, part_number=None):
        """ShowAssetTempAuthorityRequest

        The model defined in huaweicloud sdk

        :param http_verb: 分段上传时调用OBS接口的HTTP方法，具体操作需要的HTTP方法请参考OBS的接口文档。  - 初始化上传任务：POST - 上传段：PUT - 合并段：POST - 取消段：DELETE - 列举已上传段：GET
        :type http_verb: str
        :param bucket: 桶名。  调用[创建媒资：上传方式](https://support.huaweicloud.com/api-vod/vod_04_0196.html)接口中返回的响应体中的target字段获得的bucket值。
        :type bucket: str
        :param object_key: 对象名。  调用[创建媒资：上传方式](https://support.huaweicloud.com/api-vod/vod_04_0196.html)接口中返回的响应体中的target字段获得的object值。
        :type object_key: str
        :param content_type: 文件类型对应的content-type，如MP4对应video/mp4。
        :type content_type: str
        :param content_md5: 上传段时每段的MD5。
        :type content_md5: str
        :param upload_id: 每一个上传任务的id，是OBS进行初始段后OBS返回的。
        :type upload_id: str
        :param part_number: 上传段时每一段的id。  取值范围：[1,10000]。
        :type part_number: int
        """
        
        

        self._http_verb = None
        self._bucket = None
        self._object_key = None
        self._content_type = None
        self._content_md5 = None
        self._upload_id = None
        self._part_number = None
        self.discriminator = None

        self.http_verb = http_verb
        self.bucket = bucket
        self.object_key = object_key
        if content_type is not None:
            self.content_type = content_type
        if content_md5 is not None:
            self.content_md5 = content_md5
        if upload_id is not None:
            self.upload_id = upload_id
        if part_number is not None:
            self.part_number = part_number

    @property
    def http_verb(self):
        """Gets the http_verb of this ShowAssetTempAuthorityRequest.

        分段上传时调用OBS接口的HTTP方法，具体操作需要的HTTP方法请参考OBS的接口文档。  - 初始化上传任务：POST - 上传段：PUT - 合并段：POST - 取消段：DELETE - 列举已上传段：GET

        :return: The http_verb of this ShowAssetTempAuthorityRequest.
        :rtype: str
        """
        return self._http_verb

    @http_verb.setter
    def http_verb(self, http_verb):
        """Sets the http_verb of this ShowAssetTempAuthorityRequest.

        分段上传时调用OBS接口的HTTP方法，具体操作需要的HTTP方法请参考OBS的接口文档。  - 初始化上传任务：POST - 上传段：PUT - 合并段：POST - 取消段：DELETE - 列举已上传段：GET

        :param http_verb: The http_verb of this ShowAssetTempAuthorityRequest.
        :type http_verb: str
        """
        self._http_verb = http_verb

    @property
    def bucket(self):
        """Gets the bucket of this ShowAssetTempAuthorityRequest.

        桶名。  调用[创建媒资：上传方式](https://support.huaweicloud.com/api-vod/vod_04_0196.html)接口中返回的响应体中的target字段获得的bucket值。

        :return: The bucket of this ShowAssetTempAuthorityRequest.
        :rtype: str
        """
        return self._bucket

    @bucket.setter
    def bucket(self, bucket):
        """Sets the bucket of this ShowAssetTempAuthorityRequest.

        桶名。  调用[创建媒资：上传方式](https://support.huaweicloud.com/api-vod/vod_04_0196.html)接口中返回的响应体中的target字段获得的bucket值。

        :param bucket: The bucket of this ShowAssetTempAuthorityRequest.
        :type bucket: str
        """
        self._bucket = bucket

    @property
    def object_key(self):
        """Gets the object_key of this ShowAssetTempAuthorityRequest.

        对象名。  调用[创建媒资：上传方式](https://support.huaweicloud.com/api-vod/vod_04_0196.html)接口中返回的响应体中的target字段获得的object值。

        :return: The object_key of this ShowAssetTempAuthorityRequest.
        :rtype: str
        """
        return self._object_key

    @object_key.setter
    def object_key(self, object_key):
        """Sets the object_key of this ShowAssetTempAuthorityRequest.

        对象名。  调用[创建媒资：上传方式](https://support.huaweicloud.com/api-vod/vod_04_0196.html)接口中返回的响应体中的target字段获得的object值。

        :param object_key: The object_key of this ShowAssetTempAuthorityRequest.
        :type object_key: str
        """
        self._object_key = object_key

    @property
    def content_type(self):
        """Gets the content_type of this ShowAssetTempAuthorityRequest.

        文件类型对应的content-type，如MP4对应video/mp4。

        :return: The content_type of this ShowAssetTempAuthorityRequest.
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """Sets the content_type of this ShowAssetTempAuthorityRequest.

        文件类型对应的content-type，如MP4对应video/mp4。

        :param content_type: The content_type of this ShowAssetTempAuthorityRequest.
        :type content_type: str
        """
        self._content_type = content_type

    @property
    def content_md5(self):
        """Gets the content_md5 of this ShowAssetTempAuthorityRequest.

        上传段时每段的MD5。

        :return: The content_md5 of this ShowAssetTempAuthorityRequest.
        :rtype: str
        """
        return self._content_md5

    @content_md5.setter
    def content_md5(self, content_md5):
        """Sets the content_md5 of this ShowAssetTempAuthorityRequest.

        上传段时每段的MD5。

        :param content_md5: The content_md5 of this ShowAssetTempAuthorityRequest.
        :type content_md5: str
        """
        self._content_md5 = content_md5

    @property
    def upload_id(self):
        """Gets the upload_id of this ShowAssetTempAuthorityRequest.

        每一个上传任务的id，是OBS进行初始段后OBS返回的。

        :return: The upload_id of this ShowAssetTempAuthorityRequest.
        :rtype: str
        """
        return self._upload_id

    @upload_id.setter
    def upload_id(self, upload_id):
        """Sets the upload_id of this ShowAssetTempAuthorityRequest.

        每一个上传任务的id，是OBS进行初始段后OBS返回的。

        :param upload_id: The upload_id of this ShowAssetTempAuthorityRequest.
        :type upload_id: str
        """
        self._upload_id = upload_id

    @property
    def part_number(self):
        """Gets the part_number of this ShowAssetTempAuthorityRequest.

        上传段时每一段的id。  取值范围：[1,10000]。

        :return: The part_number of this ShowAssetTempAuthorityRequest.
        :rtype: int
        """
        return self._part_number

    @part_number.setter
    def part_number(self, part_number):
        """Sets the part_number of this ShowAssetTempAuthorityRequest.

        上传段时每一段的id。  取值范围：[1,10000]。

        :param part_number: The part_number of this ShowAssetTempAuthorityRequest.
        :type part_number: int
        """
        self._part_number = part_number

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
        if not isinstance(other, ShowAssetTempAuthorityRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
