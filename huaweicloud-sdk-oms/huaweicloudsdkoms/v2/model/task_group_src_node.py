# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaskGroupSrcNode:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'ak': 'str',
        'sk': 'str',
        'app_id': 'str',
        'region': 'str',
        'object_key': 'list[str]',
        'bucket': 'str',
        'cloud_type': 'str',
        'list_file': 'ListFile'
    }

    attribute_map = {
        'ak': 'ak',
        'sk': 'sk',
        'app_id': 'app_id',
        'region': 'region',
        'object_key': 'object_key',
        'bucket': 'bucket',
        'cloud_type': 'cloud_type',
        'list_file': 'list_file'
    }

    def __init__(self, ak=None, sk=None, app_id=None, region=None, object_key=None, bucket=None, cloud_type=None, list_file=None):
        """TaskGroupSrcNode

        The model defined in huaweicloud sdk

        :param ak: 源端桶的AK（最大长度100个字符），task_type为非url_list时，本参数为必选。
        :type ak: str
        :param sk: 源端桶的SK（最大长度100个字符），task_type为非url_list时，本参数为必选。
        :type sk: str
        :param app_id: 当源端为腾讯云时，需要填写此参数。
        :type app_id: str
        :param region: 源端桶所处的区域，task_type为非URL_LIST时，本参数为必选。
        :type region: str
        :param object_key: 任务类型为前缀迁移任务时，表示待迁移前缀。 整桶迁移时，此参数设置为[\&quot;\&quot;]。
        :type object_key: list[str]
        :param bucket: 源端所在桶
        :type bucket: str
        :param cloud_type: 源端云服务提供商，当task_type为URL_LIST时，本参数为URLSource。可选值有AWS、Azure、Aliyun、Tencent、HuaweiCloud、QingCloud、KingsoftCloud、Baidu、Qiniu、URLSource或者UCloud。默认值为Aliyun。
        :type cloud_type: str
        :param list_file: 
        :type list_file: :class:`huaweicloudsdkoms.v2.ListFile`
        """
        
        

        self._ak = None
        self._sk = None
        self._app_id = None
        self._region = None
        self._object_key = None
        self._bucket = None
        self._cloud_type = None
        self._list_file = None
        self.discriminator = None

        if ak is not None:
            self.ak = ak
        if sk is not None:
            self.sk = sk
        if app_id is not None:
            self.app_id = app_id
        if region is not None:
            self.region = region
        if object_key is not None:
            self.object_key = object_key
        if bucket is not None:
            self.bucket = bucket
        if cloud_type is not None:
            self.cloud_type = cloud_type
        if list_file is not None:
            self.list_file = list_file

    @property
    def ak(self):
        """Gets the ak of this TaskGroupSrcNode.

        源端桶的AK（最大长度100个字符），task_type为非url_list时，本参数为必选。

        :return: The ak of this TaskGroupSrcNode.
        :rtype: str
        """
        return self._ak

    @ak.setter
    def ak(self, ak):
        """Sets the ak of this TaskGroupSrcNode.

        源端桶的AK（最大长度100个字符），task_type为非url_list时，本参数为必选。

        :param ak: The ak of this TaskGroupSrcNode.
        :type ak: str
        """
        self._ak = ak

    @property
    def sk(self):
        """Gets the sk of this TaskGroupSrcNode.

        源端桶的SK（最大长度100个字符），task_type为非url_list时，本参数为必选。

        :return: The sk of this TaskGroupSrcNode.
        :rtype: str
        """
        return self._sk

    @sk.setter
    def sk(self, sk):
        """Sets the sk of this TaskGroupSrcNode.

        源端桶的SK（最大长度100个字符），task_type为非url_list时，本参数为必选。

        :param sk: The sk of this TaskGroupSrcNode.
        :type sk: str
        """
        self._sk = sk

    @property
    def app_id(self):
        """Gets the app_id of this TaskGroupSrcNode.

        当源端为腾讯云时，需要填写此参数。

        :return: The app_id of this TaskGroupSrcNode.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this TaskGroupSrcNode.

        当源端为腾讯云时，需要填写此参数。

        :param app_id: The app_id of this TaskGroupSrcNode.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def region(self):
        """Gets the region of this TaskGroupSrcNode.

        源端桶所处的区域，task_type为非URL_LIST时，本参数为必选。

        :return: The region of this TaskGroupSrcNode.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this TaskGroupSrcNode.

        源端桶所处的区域，task_type为非URL_LIST时，本参数为必选。

        :param region: The region of this TaskGroupSrcNode.
        :type region: str
        """
        self._region = region

    @property
    def object_key(self):
        """Gets the object_key of this TaskGroupSrcNode.

        任务类型为前缀迁移任务时，表示待迁移前缀。 整桶迁移时，此参数设置为[\"\"]。

        :return: The object_key of this TaskGroupSrcNode.
        :rtype: list[str]
        """
        return self._object_key

    @object_key.setter
    def object_key(self, object_key):
        """Sets the object_key of this TaskGroupSrcNode.

        任务类型为前缀迁移任务时，表示待迁移前缀。 整桶迁移时，此参数设置为[\"\"]。

        :param object_key: The object_key of this TaskGroupSrcNode.
        :type object_key: list[str]
        """
        self._object_key = object_key

    @property
    def bucket(self):
        """Gets the bucket of this TaskGroupSrcNode.

        源端所在桶

        :return: The bucket of this TaskGroupSrcNode.
        :rtype: str
        """
        return self._bucket

    @bucket.setter
    def bucket(self, bucket):
        """Sets the bucket of this TaskGroupSrcNode.

        源端所在桶

        :param bucket: The bucket of this TaskGroupSrcNode.
        :type bucket: str
        """
        self._bucket = bucket

    @property
    def cloud_type(self):
        """Gets the cloud_type of this TaskGroupSrcNode.

        源端云服务提供商，当task_type为URL_LIST时，本参数为URLSource。可选值有AWS、Azure、Aliyun、Tencent、HuaweiCloud、QingCloud、KingsoftCloud、Baidu、Qiniu、URLSource或者UCloud。默认值为Aliyun。

        :return: The cloud_type of this TaskGroupSrcNode.
        :rtype: str
        """
        return self._cloud_type

    @cloud_type.setter
    def cloud_type(self, cloud_type):
        """Sets the cloud_type of this TaskGroupSrcNode.

        源端云服务提供商，当task_type为URL_LIST时，本参数为URLSource。可选值有AWS、Azure、Aliyun、Tencent、HuaweiCloud、QingCloud、KingsoftCloud、Baidu、Qiniu、URLSource或者UCloud。默认值为Aliyun。

        :param cloud_type: The cloud_type of this TaskGroupSrcNode.
        :type cloud_type: str
        """
        self._cloud_type = cloud_type

    @property
    def list_file(self):
        """Gets the list_file of this TaskGroupSrcNode.


        :return: The list_file of this TaskGroupSrcNode.
        :rtype: :class:`huaweicloudsdkoms.v2.ListFile`
        """
        return self._list_file

    @list_file.setter
    def list_file(self, list_file):
        """Sets the list_file of this TaskGroupSrcNode.


        :param list_file: The list_file of this TaskGroupSrcNode.
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
        if not isinstance(other, TaskGroupSrcNode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
