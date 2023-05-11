# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SrcNodeResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'bucket': 'str',
        'cloud_type': 'str',
        'region': 'str',
        'app_id': 'str',
        'object_key': 'list[str]',
        'list_file': 'ListFile'
    }

    attribute_map = {
        'bucket': 'bucket',
        'cloud_type': 'cloud_type',
        'region': 'region',
        'app_id': 'app_id',
        'object_key': 'object_key',
        'list_file': 'list_file'
    }

    def __init__(self, bucket=None, cloud_type=None, region=None, app_id=None, object_key=None, list_file=None):
        """SrcNodeResp

        The model defined in huaweicloud sdk

        :param bucket: 源端桶的名称。
        :type bucket: str
        :param cloud_type: 源端云服务提供商。  可选值有AWS、Azure、Aliyun、Tencent、HuaweiCloud、QingCloud、KingsoftCloud、Baidu、Qiniu、URLSource或者UCloud。默认值为Aliyun。
        :type cloud_type: str
        :param region: 源端桶所处的区域。
        :type region: str
        :param app_id: 当源端为腾讯云时，会返回此参数。
        :type app_id: str
        :param object_key: 任务类型为对象迁移任务时，表示待迁移对象名称； 任务类型为前缀迁移任务时，表示待迁移前缀。
        :type object_key: list[str]
        :param list_file: 
        :type list_file: :class:`huaweicloudsdkoms.v2.ListFile`
        """
        
        

        self._bucket = None
        self._cloud_type = None
        self._region = None
        self._app_id = None
        self._object_key = None
        self._list_file = None
        self.discriminator = None

        if bucket is not None:
            self.bucket = bucket
        if cloud_type is not None:
            self.cloud_type = cloud_type
        if region is not None:
            self.region = region
        if app_id is not None:
            self.app_id = app_id
        if object_key is not None:
            self.object_key = object_key
        if list_file is not None:
            self.list_file = list_file

    @property
    def bucket(self):
        """Gets the bucket of this SrcNodeResp.

        源端桶的名称。

        :return: The bucket of this SrcNodeResp.
        :rtype: str
        """
        return self._bucket

    @bucket.setter
    def bucket(self, bucket):
        """Sets the bucket of this SrcNodeResp.

        源端桶的名称。

        :param bucket: The bucket of this SrcNodeResp.
        :type bucket: str
        """
        self._bucket = bucket

    @property
    def cloud_type(self):
        """Gets the cloud_type of this SrcNodeResp.

        源端云服务提供商。  可选值有AWS、Azure、Aliyun、Tencent、HuaweiCloud、QingCloud、KingsoftCloud、Baidu、Qiniu、URLSource或者UCloud。默认值为Aliyun。

        :return: The cloud_type of this SrcNodeResp.
        :rtype: str
        """
        return self._cloud_type

    @cloud_type.setter
    def cloud_type(self, cloud_type):
        """Sets the cloud_type of this SrcNodeResp.

        源端云服务提供商。  可选值有AWS、Azure、Aliyun、Tencent、HuaweiCloud、QingCloud、KingsoftCloud、Baidu、Qiniu、URLSource或者UCloud。默认值为Aliyun。

        :param cloud_type: The cloud_type of this SrcNodeResp.
        :type cloud_type: str
        """
        self._cloud_type = cloud_type

    @property
    def region(self):
        """Gets the region of this SrcNodeResp.

        源端桶所处的区域。

        :return: The region of this SrcNodeResp.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this SrcNodeResp.

        源端桶所处的区域。

        :param region: The region of this SrcNodeResp.
        :type region: str
        """
        self._region = region

    @property
    def app_id(self):
        """Gets the app_id of this SrcNodeResp.

        当源端为腾讯云时，会返回此参数。

        :return: The app_id of this SrcNodeResp.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this SrcNodeResp.

        当源端为腾讯云时，会返回此参数。

        :param app_id: The app_id of this SrcNodeResp.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def object_key(self):
        """Gets the object_key of this SrcNodeResp.

        任务类型为对象迁移任务时，表示待迁移对象名称； 任务类型为前缀迁移任务时，表示待迁移前缀。

        :return: The object_key of this SrcNodeResp.
        :rtype: list[str]
        """
        return self._object_key

    @object_key.setter
    def object_key(self, object_key):
        """Sets the object_key of this SrcNodeResp.

        任务类型为对象迁移任务时，表示待迁移对象名称； 任务类型为前缀迁移任务时，表示待迁移前缀。

        :param object_key: The object_key of this SrcNodeResp.
        :type object_key: list[str]
        """
        self._object_key = object_key

    @property
    def list_file(self):
        """Gets the list_file of this SrcNodeResp.

        :return: The list_file of this SrcNodeResp.
        :rtype: :class:`huaweicloudsdkoms.v2.ListFile`
        """
        return self._list_file

    @list_file.setter
    def list_file(self, list_file):
        """Sets the list_file of this SrcNodeResp.

        :param list_file: The list_file of this SrcNodeResp.
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
        if not isinstance(other, SrcNodeResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
