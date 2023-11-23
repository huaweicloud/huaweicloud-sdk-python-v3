# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowCdnInfoReq:

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
        'cloud_type': 'str',
        'region': 'str',
        'app_id': 'str',
        'bucket': 'str',
        'prefix': 'PrefixKeyInfo',
        'source_cdn': 'SourceCdnReq'
    }

    attribute_map = {
        'ak': 'ak',
        'sk': 'sk',
        'cloud_type': 'cloud_type',
        'region': 'region',
        'app_id': 'app_id',
        'bucket': 'bucket',
        'prefix': 'prefix',
        'source_cdn': 'source_cdn'
    }

    def __init__(self, ak=None, sk=None, cloud_type=None, region=None, app_id=None, bucket=None, prefix=None, source_cdn=None):
        """ShowCdnInfoReq

        The model defined in huaweicloud sdk

        :param ak: 源端桶的AK（最大长度100个字符），task_type为非url_list时，本参数为必选。
        :type ak: str
        :param sk: 源端桶的SK（最大长度100个字符），task_type为非url_list时，本参数为必选。
        :type sk: str
        :param cloud_type: 云类型 AWS：亚马逊 Aliyun：阿里云 Qiniu：七牛云 QingCloud：青云 Tencent：腾讯云 Baidu：百度云 KingsoftCloud：金山云 Azure：微软云 UCloud：优刻得 HuaweiCloud：华为云 URLSource：URL HEC：HEC
        :type cloud_type: str
        :param region: 区域
        :type region: str
        :param app_id: 当源端为腾讯云时，会返回此参数。
        :type app_id: str
        :param bucket: 桶名
        :type bucket: str
        :param prefix: 
        :type prefix: :class:`huaweicloudsdkoms.v2.PrefixKeyInfo`
        :param source_cdn: 
        :type source_cdn: :class:`huaweicloudsdkoms.v2.SourceCdnReq`
        """
        
        

        self._ak = None
        self._sk = None
        self._cloud_type = None
        self._region = None
        self._app_id = None
        self._bucket = None
        self._prefix = None
        self._source_cdn = None
        self.discriminator = None

        self.ak = ak
        self.sk = sk
        self.cloud_type = cloud_type
        self.region = region
        if app_id is not None:
            self.app_id = app_id
        self.bucket = bucket
        if prefix is not None:
            self.prefix = prefix
        self.source_cdn = source_cdn

    @property
    def ak(self):
        """Gets the ak of this ShowCdnInfoReq.

        源端桶的AK（最大长度100个字符），task_type为非url_list时，本参数为必选。

        :return: The ak of this ShowCdnInfoReq.
        :rtype: str
        """
        return self._ak

    @ak.setter
    def ak(self, ak):
        """Sets the ak of this ShowCdnInfoReq.

        源端桶的AK（最大长度100个字符），task_type为非url_list时，本参数为必选。

        :param ak: The ak of this ShowCdnInfoReq.
        :type ak: str
        """
        self._ak = ak

    @property
    def sk(self):
        """Gets the sk of this ShowCdnInfoReq.

        源端桶的SK（最大长度100个字符），task_type为非url_list时，本参数为必选。

        :return: The sk of this ShowCdnInfoReq.
        :rtype: str
        """
        return self._sk

    @sk.setter
    def sk(self, sk):
        """Sets the sk of this ShowCdnInfoReq.

        源端桶的SK（最大长度100个字符），task_type为非url_list时，本参数为必选。

        :param sk: The sk of this ShowCdnInfoReq.
        :type sk: str
        """
        self._sk = sk

    @property
    def cloud_type(self):
        """Gets the cloud_type of this ShowCdnInfoReq.

        云类型 AWS：亚马逊 Aliyun：阿里云 Qiniu：七牛云 QingCloud：青云 Tencent：腾讯云 Baidu：百度云 KingsoftCloud：金山云 Azure：微软云 UCloud：优刻得 HuaweiCloud：华为云 URLSource：URL HEC：HEC

        :return: The cloud_type of this ShowCdnInfoReq.
        :rtype: str
        """
        return self._cloud_type

    @cloud_type.setter
    def cloud_type(self, cloud_type):
        """Sets the cloud_type of this ShowCdnInfoReq.

        云类型 AWS：亚马逊 Aliyun：阿里云 Qiniu：七牛云 QingCloud：青云 Tencent：腾讯云 Baidu：百度云 KingsoftCloud：金山云 Azure：微软云 UCloud：优刻得 HuaweiCloud：华为云 URLSource：URL HEC：HEC

        :param cloud_type: The cloud_type of this ShowCdnInfoReq.
        :type cloud_type: str
        """
        self._cloud_type = cloud_type

    @property
    def region(self):
        """Gets the region of this ShowCdnInfoReq.

        区域

        :return: The region of this ShowCdnInfoReq.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this ShowCdnInfoReq.

        区域

        :param region: The region of this ShowCdnInfoReq.
        :type region: str
        """
        self._region = region

    @property
    def app_id(self):
        """Gets the app_id of this ShowCdnInfoReq.

        当源端为腾讯云时，会返回此参数。

        :return: The app_id of this ShowCdnInfoReq.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this ShowCdnInfoReq.

        当源端为腾讯云时，会返回此参数。

        :param app_id: The app_id of this ShowCdnInfoReq.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def bucket(self):
        """Gets the bucket of this ShowCdnInfoReq.

        桶名

        :return: The bucket of this ShowCdnInfoReq.
        :rtype: str
        """
        return self._bucket

    @bucket.setter
    def bucket(self, bucket):
        """Sets the bucket of this ShowCdnInfoReq.

        桶名

        :param bucket: The bucket of this ShowCdnInfoReq.
        :type bucket: str
        """
        self._bucket = bucket

    @property
    def prefix(self):
        """Gets the prefix of this ShowCdnInfoReq.

        :return: The prefix of this ShowCdnInfoReq.
        :rtype: :class:`huaweicloudsdkoms.v2.PrefixKeyInfo`
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        """Sets the prefix of this ShowCdnInfoReq.

        :param prefix: The prefix of this ShowCdnInfoReq.
        :type prefix: :class:`huaweicloudsdkoms.v2.PrefixKeyInfo`
        """
        self._prefix = prefix

    @property
    def source_cdn(self):
        """Gets the source_cdn of this ShowCdnInfoReq.

        :return: The source_cdn of this ShowCdnInfoReq.
        :rtype: :class:`huaweicloudsdkoms.v2.SourceCdnReq`
        """
        return self._source_cdn

    @source_cdn.setter
    def source_cdn(self, source_cdn):
        """Sets the source_cdn of this ShowCdnInfoReq.

        :param source_cdn: The source_cdn of this ShowCdnInfoReq.
        :type source_cdn: :class:`huaweicloudsdkoms.v2.SourceCdnReq`
        """
        self._source_cdn = source_cdn

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
        if not isinstance(other, ShowCdnInfoReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
