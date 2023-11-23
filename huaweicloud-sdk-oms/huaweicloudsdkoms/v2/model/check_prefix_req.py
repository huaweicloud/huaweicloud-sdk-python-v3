# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CheckPrefixReq:

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
        'ak': 'str',
        'sk': 'str',
        'app_id': 'str',
        'bucket_name': 'str',
        'file_name': 'str',
        'data_center': 'str',
        'security_token': 'str'
    }

    attribute_map = {
        'cloud_type': 'cloud_type',
        'ak': 'ak',
        'sk': 'sk',
        'app_id': 'app_id',
        'bucket_name': 'bucket_name',
        'file_name': 'file_name',
        'data_center': 'data_center',
        'security_token': 'security_token'
    }

    def __init__(self, cloud_type=None, ak=None, sk=None, app_id=None, bucket_name=None, file_name=None, data_center=None, security_token=None):
        """CheckPrefixReq

        The model defined in huaweicloud sdk

        :param cloud_type: 云类型 AWS：亚马逊 Aliyun：阿里云 Qiniu：七牛云 QingCloud：青云 Tencent：腾讯云 Baidu：百度云 KingsoftCloud：金山云 Azure：微软云 UCloud：优刻得 HuaweiCloud：华为云 URLSource：URL HEC：HEC
        :type cloud_type: str
        :param ak: 源端桶的AK（最大长度100个字符），task_type为非url_list时，本参数为必选。
        :type ak: str
        :param sk: 源端桶的SK（最大长度100个字符），task_type为非url_list时，本参数为必选。
        :type sk: str
        :param app_id: 当源端为腾讯云时，会返回此参数。
        :type app_id: str
        :param bucket_name: 桶名
        :type bucket_name: str
        :param file_name: 前缀名称
        :type file_name: str
        :param data_center: 数据中心，区域
        :type data_center: str
        :param security_token: 安全令牌
        :type security_token: str
        """
        
        

        self._cloud_type = None
        self._ak = None
        self._sk = None
        self._app_id = None
        self._bucket_name = None
        self._file_name = None
        self._data_center = None
        self._security_token = None
        self.discriminator = None

        self.cloud_type = cloud_type
        if ak is not None:
            self.ak = ak
        if sk is not None:
            self.sk = sk
        if app_id is not None:
            self.app_id = app_id
        self.bucket_name = bucket_name
        self.file_name = file_name
        self.data_center = data_center
        if security_token is not None:
            self.security_token = security_token

    @property
    def cloud_type(self):
        """Gets the cloud_type of this CheckPrefixReq.

        云类型 AWS：亚马逊 Aliyun：阿里云 Qiniu：七牛云 QingCloud：青云 Tencent：腾讯云 Baidu：百度云 KingsoftCloud：金山云 Azure：微软云 UCloud：优刻得 HuaweiCloud：华为云 URLSource：URL HEC：HEC

        :return: The cloud_type of this CheckPrefixReq.
        :rtype: str
        """
        return self._cloud_type

    @cloud_type.setter
    def cloud_type(self, cloud_type):
        """Sets the cloud_type of this CheckPrefixReq.

        云类型 AWS：亚马逊 Aliyun：阿里云 Qiniu：七牛云 QingCloud：青云 Tencent：腾讯云 Baidu：百度云 KingsoftCloud：金山云 Azure：微软云 UCloud：优刻得 HuaweiCloud：华为云 URLSource：URL HEC：HEC

        :param cloud_type: The cloud_type of this CheckPrefixReq.
        :type cloud_type: str
        """
        self._cloud_type = cloud_type

    @property
    def ak(self):
        """Gets the ak of this CheckPrefixReq.

        源端桶的AK（最大长度100个字符），task_type为非url_list时，本参数为必选。

        :return: The ak of this CheckPrefixReq.
        :rtype: str
        """
        return self._ak

    @ak.setter
    def ak(self, ak):
        """Sets the ak of this CheckPrefixReq.

        源端桶的AK（最大长度100个字符），task_type为非url_list时，本参数为必选。

        :param ak: The ak of this CheckPrefixReq.
        :type ak: str
        """
        self._ak = ak

    @property
    def sk(self):
        """Gets the sk of this CheckPrefixReq.

        源端桶的SK（最大长度100个字符），task_type为非url_list时，本参数为必选。

        :return: The sk of this CheckPrefixReq.
        :rtype: str
        """
        return self._sk

    @sk.setter
    def sk(self, sk):
        """Sets the sk of this CheckPrefixReq.

        源端桶的SK（最大长度100个字符），task_type为非url_list时，本参数为必选。

        :param sk: The sk of this CheckPrefixReq.
        :type sk: str
        """
        self._sk = sk

    @property
    def app_id(self):
        """Gets the app_id of this CheckPrefixReq.

        当源端为腾讯云时，会返回此参数。

        :return: The app_id of this CheckPrefixReq.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this CheckPrefixReq.

        当源端为腾讯云时，会返回此参数。

        :param app_id: The app_id of this CheckPrefixReq.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def bucket_name(self):
        """Gets the bucket_name of this CheckPrefixReq.

        桶名

        :return: The bucket_name of this CheckPrefixReq.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        """Sets the bucket_name of this CheckPrefixReq.

        桶名

        :param bucket_name: The bucket_name of this CheckPrefixReq.
        :type bucket_name: str
        """
        self._bucket_name = bucket_name

    @property
    def file_name(self):
        """Gets the file_name of this CheckPrefixReq.

        前缀名称

        :return: The file_name of this CheckPrefixReq.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this CheckPrefixReq.

        前缀名称

        :param file_name: The file_name of this CheckPrefixReq.
        :type file_name: str
        """
        self._file_name = file_name

    @property
    def data_center(self):
        """Gets the data_center of this CheckPrefixReq.

        数据中心，区域

        :return: The data_center of this CheckPrefixReq.
        :rtype: str
        """
        return self._data_center

    @data_center.setter
    def data_center(self, data_center):
        """Sets the data_center of this CheckPrefixReq.

        数据中心，区域

        :param data_center: The data_center of this CheckPrefixReq.
        :type data_center: str
        """
        self._data_center = data_center

    @property
    def security_token(self):
        """Gets the security_token of this CheckPrefixReq.

        安全令牌

        :return: The security_token of this CheckPrefixReq.
        :rtype: str
        """
        return self._security_token

    @security_token.setter
    def security_token(self, security_token):
        """Sets the security_token of this CheckPrefixReq.

        安全令牌

        :param security_token: The security_token of this CheckPrefixReq.
        :type security_token: str
        """
        self._security_token = security_token

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
        if not isinstance(other, CheckPrefixReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
