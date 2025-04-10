# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowBucketReq:

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
        'file_path': 'str',
        'ak': 'str',
        'sk': 'str',
        'json_auth_file': 'str',
        'data_center': 'str',
        'page_size': 'int',
        'behind_filename': 'str',
        'app_id': 'str',
        'bucket_name': 'str'
    }

    attribute_map = {
        'cloud_type': 'cloud_type',
        'file_path': 'file_path',
        'ak': 'ak',
        'sk': 'sk',
        'json_auth_file': 'json_auth_file',
        'data_center': 'data_center',
        'page_size': 'page_size',
        'behind_filename': 'behind_filename',
        'app_id': 'app_id',
        'bucket_name': 'bucket_name'
    }

    def __init__(self, cloud_type=None, file_path=None, ak=None, sk=None, json_auth_file=None, data_center=None, page_size=None, behind_filename=None, app_id=None, bucket_name=None):
        r"""ShowBucketReq

        The model defined in huaweicloud sdk

        :param cloud_type: 云类型 AWS：亚马逊 Aliyun：阿里云 Qiniu：七牛云 QingCloud：青云 Tencent：腾讯云 Baidu：百度云 KingsoftCloud：金山云 Azure：微软云 UCloud：优刻得 HuaweiCloud：华为云 Google: 谷歌云 URLSource：URL HEC：HEC
        :type cloud_type: str
        :param file_path: 目标桶中需要查询的对象文件路径，/结尾
        :type file_path: str
        :param ak: 源端桶的AK（最大长度100个字符）
        :type ak: str
        :param sk: 源端桶的SK（最大长度100个字符）
        :type sk: str
        :param json_auth_file: 用于谷歌云Cloud Storage鉴权
        :type json_auth_file: str
        :param data_center: 数据中心，区域
        :type data_center: str
        :param page_size: 分页信息，页大小
        :type page_size: int
        :param behind_filename: 分页信息，当前页最后一个对象名称（偏移量）
        :type behind_filename: str
        :param app_id: 当源端为腾讯云时，会返回此参数。
        :type app_id: str
        :param bucket_name: 桶名
        :type bucket_name: str
        """
        
        

        self._cloud_type = None
        self._file_path = None
        self._ak = None
        self._sk = None
        self._json_auth_file = None
        self._data_center = None
        self._page_size = None
        self._behind_filename = None
        self._app_id = None
        self._bucket_name = None
        self.discriminator = None

        self.cloud_type = cloud_type
        self.file_path = file_path
        if ak is not None:
            self.ak = ak
        if sk is not None:
            self.sk = sk
        if json_auth_file is not None:
            self.json_auth_file = json_auth_file
        self.data_center = data_center
        self.page_size = page_size
        self.behind_filename = behind_filename
        if app_id is not None:
            self.app_id = app_id
        self.bucket_name = bucket_name

    @property
    def cloud_type(self):
        r"""Gets the cloud_type of this ShowBucketReq.

        云类型 AWS：亚马逊 Aliyun：阿里云 Qiniu：七牛云 QingCloud：青云 Tencent：腾讯云 Baidu：百度云 KingsoftCloud：金山云 Azure：微软云 UCloud：优刻得 HuaweiCloud：华为云 Google: 谷歌云 URLSource：URL HEC：HEC

        :return: The cloud_type of this ShowBucketReq.
        :rtype: str
        """
        return self._cloud_type

    @cloud_type.setter
    def cloud_type(self, cloud_type):
        r"""Sets the cloud_type of this ShowBucketReq.

        云类型 AWS：亚马逊 Aliyun：阿里云 Qiniu：七牛云 QingCloud：青云 Tencent：腾讯云 Baidu：百度云 KingsoftCloud：金山云 Azure：微软云 UCloud：优刻得 HuaweiCloud：华为云 Google: 谷歌云 URLSource：URL HEC：HEC

        :param cloud_type: The cloud_type of this ShowBucketReq.
        :type cloud_type: str
        """
        self._cloud_type = cloud_type

    @property
    def file_path(self):
        r"""Gets the file_path of this ShowBucketReq.

        目标桶中需要查询的对象文件路径，/结尾

        :return: The file_path of this ShowBucketReq.
        :rtype: str
        """
        return self._file_path

    @file_path.setter
    def file_path(self, file_path):
        r"""Sets the file_path of this ShowBucketReq.

        目标桶中需要查询的对象文件路径，/结尾

        :param file_path: The file_path of this ShowBucketReq.
        :type file_path: str
        """
        self._file_path = file_path

    @property
    def ak(self):
        r"""Gets the ak of this ShowBucketReq.

        源端桶的AK（最大长度100个字符）

        :return: The ak of this ShowBucketReq.
        :rtype: str
        """
        return self._ak

    @ak.setter
    def ak(self, ak):
        r"""Sets the ak of this ShowBucketReq.

        源端桶的AK（最大长度100个字符）

        :param ak: The ak of this ShowBucketReq.
        :type ak: str
        """
        self._ak = ak

    @property
    def sk(self):
        r"""Gets the sk of this ShowBucketReq.

        源端桶的SK（最大长度100个字符）

        :return: The sk of this ShowBucketReq.
        :rtype: str
        """
        return self._sk

    @sk.setter
    def sk(self, sk):
        r"""Sets the sk of this ShowBucketReq.

        源端桶的SK（最大长度100个字符）

        :param sk: The sk of this ShowBucketReq.
        :type sk: str
        """
        self._sk = sk

    @property
    def json_auth_file(self):
        r"""Gets the json_auth_file of this ShowBucketReq.

        用于谷歌云Cloud Storage鉴权

        :return: The json_auth_file of this ShowBucketReq.
        :rtype: str
        """
        return self._json_auth_file

    @json_auth_file.setter
    def json_auth_file(self, json_auth_file):
        r"""Sets the json_auth_file of this ShowBucketReq.

        用于谷歌云Cloud Storage鉴权

        :param json_auth_file: The json_auth_file of this ShowBucketReq.
        :type json_auth_file: str
        """
        self._json_auth_file = json_auth_file

    @property
    def data_center(self):
        r"""Gets the data_center of this ShowBucketReq.

        数据中心，区域

        :return: The data_center of this ShowBucketReq.
        :rtype: str
        """
        return self._data_center

    @data_center.setter
    def data_center(self, data_center):
        r"""Sets the data_center of this ShowBucketReq.

        数据中心，区域

        :param data_center: The data_center of this ShowBucketReq.
        :type data_center: str
        """
        self._data_center = data_center

    @property
    def page_size(self):
        r"""Gets the page_size of this ShowBucketReq.

        分页信息，页大小

        :return: The page_size of this ShowBucketReq.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        r"""Sets the page_size of this ShowBucketReq.

        分页信息，页大小

        :param page_size: The page_size of this ShowBucketReq.
        :type page_size: int
        """
        self._page_size = page_size

    @property
    def behind_filename(self):
        r"""Gets the behind_filename of this ShowBucketReq.

        分页信息，当前页最后一个对象名称（偏移量）

        :return: The behind_filename of this ShowBucketReq.
        :rtype: str
        """
        return self._behind_filename

    @behind_filename.setter
    def behind_filename(self, behind_filename):
        r"""Sets the behind_filename of this ShowBucketReq.

        分页信息，当前页最后一个对象名称（偏移量）

        :param behind_filename: The behind_filename of this ShowBucketReq.
        :type behind_filename: str
        """
        self._behind_filename = behind_filename

    @property
    def app_id(self):
        r"""Gets the app_id of this ShowBucketReq.

        当源端为腾讯云时，会返回此参数。

        :return: The app_id of this ShowBucketReq.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        r"""Sets the app_id of this ShowBucketReq.

        当源端为腾讯云时，会返回此参数。

        :param app_id: The app_id of this ShowBucketReq.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def bucket_name(self):
        r"""Gets the bucket_name of this ShowBucketReq.

        桶名

        :return: The bucket_name of this ShowBucketReq.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        r"""Sets the bucket_name of this ShowBucketReq.

        桶名

        :param bucket_name: The bucket_name of this ShowBucketReq.
        :type bucket_name: str
        """
        self._bucket_name = bucket_name

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
        if not isinstance(other, ShowBucketReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
