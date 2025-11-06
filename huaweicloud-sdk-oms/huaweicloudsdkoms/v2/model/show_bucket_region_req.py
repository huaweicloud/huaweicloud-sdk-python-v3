# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowBucketRegionReq:

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
        'json_auth_file': 'str',
        'connection_string': 'str',
        'app_id': 'str',
        'bucket_name': 'str'
    }

    attribute_map = {
        'cloud_type': 'cloud_type',
        'ak': 'ak',
        'sk': 'sk',
        'json_auth_file': 'json_auth_file',
        'connection_string': 'connection_string',
        'app_id': 'app_id',
        'bucket_name': 'bucket_name'
    }

    def __init__(self, cloud_type=None, ak=None, sk=None, json_auth_file=None, connection_string=None, app_id=None, bucket_name=None):
        r"""ShowBucketRegionReq

        The model defined in huaweicloud sdk

        :param cloud_type: 云类型 AWS：亚马逊 Aliyun：阿里云 Qiniu：七牛云 QingCloud：青云 Tencent：腾讯云 Baidu：百度云 KingsoftCloud：金山云 Azure：微软云 UCloud：优刻得 HuaweiCloud：华为云 Google: 谷歌云 URLSource：URL HEC：HEC
        :type cloud_type: str
        :param ak: 源端桶的AK（最大长度100个字符），task_type为非url_list时，本参数为必选。
        :type ak: str
        :param sk: 源端桶的SK（最大长度100个字符），task_type为非url_list时，本参数为必选。
        :type sk: str
        :param json_auth_file: 用于谷歌云Cloud Storage鉴权
        :type json_auth_file: str
        :param connection_string: 连接字符串，用于微软云Blob鉴权
        :type connection_string: str
        :param app_id: 当源端为腾讯云时，会返回此参数。
        :type app_id: str
        :param bucket_name: 桶名
        :type bucket_name: str
        """
        
        

        self._cloud_type = None
        self._ak = None
        self._sk = None
        self._json_auth_file = None
        self._connection_string = None
        self._app_id = None
        self._bucket_name = None
        self.discriminator = None

        self.cloud_type = cloud_type
        if ak is not None:
            self.ak = ak
        if sk is not None:
            self.sk = sk
        if json_auth_file is not None:
            self.json_auth_file = json_auth_file
        if connection_string is not None:
            self.connection_string = connection_string
        if app_id is not None:
            self.app_id = app_id
        self.bucket_name = bucket_name

    @property
    def cloud_type(self):
        r"""Gets the cloud_type of this ShowBucketRegionReq.

        云类型 AWS：亚马逊 Aliyun：阿里云 Qiniu：七牛云 QingCloud：青云 Tencent：腾讯云 Baidu：百度云 KingsoftCloud：金山云 Azure：微软云 UCloud：优刻得 HuaweiCloud：华为云 Google: 谷歌云 URLSource：URL HEC：HEC

        :return: The cloud_type of this ShowBucketRegionReq.
        :rtype: str
        """
        return self._cloud_type

    @cloud_type.setter
    def cloud_type(self, cloud_type):
        r"""Sets the cloud_type of this ShowBucketRegionReq.

        云类型 AWS：亚马逊 Aliyun：阿里云 Qiniu：七牛云 QingCloud：青云 Tencent：腾讯云 Baidu：百度云 KingsoftCloud：金山云 Azure：微软云 UCloud：优刻得 HuaweiCloud：华为云 Google: 谷歌云 URLSource：URL HEC：HEC

        :param cloud_type: The cloud_type of this ShowBucketRegionReq.
        :type cloud_type: str
        """
        self._cloud_type = cloud_type

    @property
    def ak(self):
        r"""Gets the ak of this ShowBucketRegionReq.

        源端桶的AK（最大长度100个字符），task_type为非url_list时，本参数为必选。

        :return: The ak of this ShowBucketRegionReq.
        :rtype: str
        """
        return self._ak

    @ak.setter
    def ak(self, ak):
        r"""Sets the ak of this ShowBucketRegionReq.

        源端桶的AK（最大长度100个字符），task_type为非url_list时，本参数为必选。

        :param ak: The ak of this ShowBucketRegionReq.
        :type ak: str
        """
        self._ak = ak

    @property
    def sk(self):
        r"""Gets the sk of this ShowBucketRegionReq.

        源端桶的SK（最大长度100个字符），task_type为非url_list时，本参数为必选。

        :return: The sk of this ShowBucketRegionReq.
        :rtype: str
        """
        return self._sk

    @sk.setter
    def sk(self, sk):
        r"""Sets the sk of this ShowBucketRegionReq.

        源端桶的SK（最大长度100个字符），task_type为非url_list时，本参数为必选。

        :param sk: The sk of this ShowBucketRegionReq.
        :type sk: str
        """
        self._sk = sk

    @property
    def json_auth_file(self):
        r"""Gets the json_auth_file of this ShowBucketRegionReq.

        用于谷歌云Cloud Storage鉴权

        :return: The json_auth_file of this ShowBucketRegionReq.
        :rtype: str
        """
        return self._json_auth_file

    @json_auth_file.setter
    def json_auth_file(self, json_auth_file):
        r"""Sets the json_auth_file of this ShowBucketRegionReq.

        用于谷歌云Cloud Storage鉴权

        :param json_auth_file: The json_auth_file of this ShowBucketRegionReq.
        :type json_auth_file: str
        """
        self._json_auth_file = json_auth_file

    @property
    def connection_string(self):
        r"""Gets the connection_string of this ShowBucketRegionReq.

        连接字符串，用于微软云Blob鉴权

        :return: The connection_string of this ShowBucketRegionReq.
        :rtype: str
        """
        return self._connection_string

    @connection_string.setter
    def connection_string(self, connection_string):
        r"""Sets the connection_string of this ShowBucketRegionReq.

        连接字符串，用于微软云Blob鉴权

        :param connection_string: The connection_string of this ShowBucketRegionReq.
        :type connection_string: str
        """
        self._connection_string = connection_string

    @property
    def app_id(self):
        r"""Gets the app_id of this ShowBucketRegionReq.

        当源端为腾讯云时，会返回此参数。

        :return: The app_id of this ShowBucketRegionReq.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        r"""Sets the app_id of this ShowBucketRegionReq.

        当源端为腾讯云时，会返回此参数。

        :param app_id: The app_id of this ShowBucketRegionReq.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def bucket_name(self):
        r"""Gets the bucket_name of this ShowBucketRegionReq.

        桶名

        :return: The bucket_name of this ShowBucketRegionReq.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        r"""Sets the bucket_name of this ShowBucketRegionReq.

        桶名

        :param bucket_name: The bucket_name of this ShowBucketRegionReq.
        :type bucket_name: str
        """
        self._bucket_name = bucket_name

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ShowBucketRegionReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
