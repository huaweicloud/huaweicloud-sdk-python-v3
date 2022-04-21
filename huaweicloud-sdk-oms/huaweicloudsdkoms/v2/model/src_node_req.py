# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SrcNodeReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'cloud_type': 'str',
        'region': 'str',
        'ak': 'str',
        'sk': 'str',
        'security_token': 'str',
        'app_id': 'str',
        'bucket': 'str',
        'object_key': 'list[str]',
        'list_file': 'ListFile'
    }

    attribute_map = {
        'cloud_type': 'cloud_type',
        'region': 'region',
        'ak': 'ak',
        'sk': 'sk',
        'security_token': 'security_token',
        'app_id': 'app_id',
        'bucket': 'bucket',
        'object_key': 'object_key',
        'list_file': 'list_file'
    }

    def __init__(self, cloud_type=None, region=None, ak=None, sk=None, security_token=None, app_id=None, bucket=None, object_key=None, list_file=None):
        """SrcNodeReq

        The model defined in huaweicloud sdk

        :param cloud_type: 源端云服务提供商，task_type为非url_list时，本参数为URLSource。  可选值有AWS、Azure、Aliyun、Tencent、HuaweiCloud、QingCloud、KingsoftCloud、Baidu、Qiniu、URLSource或者UCloud。默认值为Aliyun。
        :type cloud_type: str
        :param region: 源端桶所处的区域，task_type为非url_list时，本参数为必选。
        :type region: str
        :param ak: 源端桶的AK（最大长度100个字符），task_type为非url_list时，本参数为必选。
        :type ak: str
        :param sk: 源端桶的SK（最大长度100个字符），task_type为非url_list时，本参数为必选。
        :type sk: str
        :param security_token: 源端桶的临时Token（最大长度16384个字符）
        :type security_token: str
        :param app_id: 当源端为腾讯云时，需要填写此参数。
        :type app_id: str
        :param bucket: 源端桶的名称，task_type为非url_list时，本参数为必选。
        :type bucket: str
        :param object_key: 任务类型为对象迁移任务时，表示待迁移对象名称（以“/”结尾的字符串代表待迁移的文件夹，非“/”结尾的字符串代表待迁移的文件。）； 任务类型为前缀迁移任务时，表示待迁移前缀。 整桶迁移时，此参数设置为[\&quot;\&quot;]。
        :type object_key: list[str]
        :param list_file: 
        :type list_file: :class:`huaweicloudsdkoms.v2.ListFile`
        """
        
        

        self._cloud_type = None
        self._region = None
        self._ak = None
        self._sk = None
        self._security_token = None
        self._app_id = None
        self._bucket = None
        self._object_key = None
        self._list_file = None
        self.discriminator = None

        if cloud_type is not None:
            self.cloud_type = cloud_type
        if region is not None:
            self.region = region
        if ak is not None:
            self.ak = ak
        if sk is not None:
            self.sk = sk
        if security_token is not None:
            self.security_token = security_token
        if app_id is not None:
            self.app_id = app_id
        if bucket is not None:
            self.bucket = bucket
        if object_key is not None:
            self.object_key = object_key
        if list_file is not None:
            self.list_file = list_file

    @property
    def cloud_type(self):
        """Gets the cloud_type of this SrcNodeReq.

        源端云服务提供商，task_type为非url_list时，本参数为URLSource。  可选值有AWS、Azure、Aliyun、Tencent、HuaweiCloud、QingCloud、KingsoftCloud、Baidu、Qiniu、URLSource或者UCloud。默认值为Aliyun。

        :return: The cloud_type of this SrcNodeReq.
        :rtype: str
        """
        return self._cloud_type

    @cloud_type.setter
    def cloud_type(self, cloud_type):
        """Sets the cloud_type of this SrcNodeReq.

        源端云服务提供商，task_type为非url_list时，本参数为URLSource。  可选值有AWS、Azure、Aliyun、Tencent、HuaweiCloud、QingCloud、KingsoftCloud、Baidu、Qiniu、URLSource或者UCloud。默认值为Aliyun。

        :param cloud_type: The cloud_type of this SrcNodeReq.
        :type cloud_type: str
        """
        self._cloud_type = cloud_type

    @property
    def region(self):
        """Gets the region of this SrcNodeReq.

        源端桶所处的区域，task_type为非url_list时，本参数为必选。

        :return: The region of this SrcNodeReq.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this SrcNodeReq.

        源端桶所处的区域，task_type为非url_list时，本参数为必选。

        :param region: The region of this SrcNodeReq.
        :type region: str
        """
        self._region = region

    @property
    def ak(self):
        """Gets the ak of this SrcNodeReq.

        源端桶的AK（最大长度100个字符），task_type为非url_list时，本参数为必选。

        :return: The ak of this SrcNodeReq.
        :rtype: str
        """
        return self._ak

    @ak.setter
    def ak(self, ak):
        """Sets the ak of this SrcNodeReq.

        源端桶的AK（最大长度100个字符），task_type为非url_list时，本参数为必选。

        :param ak: The ak of this SrcNodeReq.
        :type ak: str
        """
        self._ak = ak

    @property
    def sk(self):
        """Gets the sk of this SrcNodeReq.

        源端桶的SK（最大长度100个字符），task_type为非url_list时，本参数为必选。

        :return: The sk of this SrcNodeReq.
        :rtype: str
        """
        return self._sk

    @sk.setter
    def sk(self, sk):
        """Sets the sk of this SrcNodeReq.

        源端桶的SK（最大长度100个字符），task_type为非url_list时，本参数为必选。

        :param sk: The sk of this SrcNodeReq.
        :type sk: str
        """
        self._sk = sk

    @property
    def security_token(self):
        """Gets the security_token of this SrcNodeReq.

        源端桶的临时Token（最大长度16384个字符）

        :return: The security_token of this SrcNodeReq.
        :rtype: str
        """
        return self._security_token

    @security_token.setter
    def security_token(self, security_token):
        """Sets the security_token of this SrcNodeReq.

        源端桶的临时Token（最大长度16384个字符）

        :param security_token: The security_token of this SrcNodeReq.
        :type security_token: str
        """
        self._security_token = security_token

    @property
    def app_id(self):
        """Gets the app_id of this SrcNodeReq.

        当源端为腾讯云时，需要填写此参数。

        :return: The app_id of this SrcNodeReq.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this SrcNodeReq.

        当源端为腾讯云时，需要填写此参数。

        :param app_id: The app_id of this SrcNodeReq.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def bucket(self):
        """Gets the bucket of this SrcNodeReq.

        源端桶的名称，task_type为非url_list时，本参数为必选。

        :return: The bucket of this SrcNodeReq.
        :rtype: str
        """
        return self._bucket

    @bucket.setter
    def bucket(self, bucket):
        """Sets the bucket of this SrcNodeReq.

        源端桶的名称，task_type为非url_list时，本参数为必选。

        :param bucket: The bucket of this SrcNodeReq.
        :type bucket: str
        """
        self._bucket = bucket

    @property
    def object_key(self):
        """Gets the object_key of this SrcNodeReq.

        任务类型为对象迁移任务时，表示待迁移对象名称（以“/”结尾的字符串代表待迁移的文件夹，非“/”结尾的字符串代表待迁移的文件。）； 任务类型为前缀迁移任务时，表示待迁移前缀。 整桶迁移时，此参数设置为[\"\"]。

        :return: The object_key of this SrcNodeReq.
        :rtype: list[str]
        """
        return self._object_key

    @object_key.setter
    def object_key(self, object_key):
        """Sets the object_key of this SrcNodeReq.

        任务类型为对象迁移任务时，表示待迁移对象名称（以“/”结尾的字符串代表待迁移的文件夹，非“/”结尾的字符串代表待迁移的文件。）； 任务类型为前缀迁移任务时，表示待迁移前缀。 整桶迁移时，此参数设置为[\"\"]。

        :param object_key: The object_key of this SrcNodeReq.
        :type object_key: list[str]
        """
        self._object_key = object_key

    @property
    def list_file(self):
        """Gets the list_file of this SrcNodeReq.


        :return: The list_file of this SrcNodeReq.
        :rtype: :class:`huaweicloudsdkoms.v2.ListFile`
        """
        return self._list_file

    @list_file.setter
    def list_file(self, list_file):
        """Sets the list_file of this SrcNodeReq.


        :param list_file: The list_file of this SrcNodeReq.
        :type list_file: :class:`huaweicloudsdkoms.v2.ListFile`
        """
        self._list_file = list_file

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
        if not isinstance(other, SrcNodeReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
