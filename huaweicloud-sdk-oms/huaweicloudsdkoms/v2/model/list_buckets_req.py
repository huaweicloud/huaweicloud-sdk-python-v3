# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListBucketsReq:

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
        'app_id': 'str'
    }

    attribute_map = {
        'cloud_type': 'cloud_type',
        'ak': 'ak',
        'sk': 'sk',
        'app_id': 'app_id'
    }

    def __init__(self, cloud_type=None, ak=None, sk=None, app_id=None):
        """ListBucketsReq

        The model defined in huaweicloud sdk

        :param cloud_type: 云类型 AWS：亚马逊 Aliyun：阿里云 Qiniu：七牛云 QingCloud：青云 Tencent：腾讯云 Baidu：百度云 KingsoftCloud：金山云 Azure：微软云 UCloud：优刻得 HuaweiCloud：华为云 URLSource：URL HEC：HEC
        :type cloud_type: str
        :param ak: 源端桶的AK（最大长度100个字符），task_type为非url_list时，本参数为必选。
        :type ak: str
        :param sk: 源端桶的SK（最大长度100个字符），task_type为非url_list时，本参数为必选。
        :type sk: str
        :param app_id: 当源端为腾讯云时，会返回此参数。
        :type app_id: str
        """
        
        

        self._cloud_type = None
        self._ak = None
        self._sk = None
        self._app_id = None
        self.discriminator = None

        self.cloud_type = cloud_type
        if ak is not None:
            self.ak = ak
        if sk is not None:
            self.sk = sk
        if app_id is not None:
            self.app_id = app_id

    @property
    def cloud_type(self):
        """Gets the cloud_type of this ListBucketsReq.

        云类型 AWS：亚马逊 Aliyun：阿里云 Qiniu：七牛云 QingCloud：青云 Tencent：腾讯云 Baidu：百度云 KingsoftCloud：金山云 Azure：微软云 UCloud：优刻得 HuaweiCloud：华为云 URLSource：URL HEC：HEC

        :return: The cloud_type of this ListBucketsReq.
        :rtype: str
        """
        return self._cloud_type

    @cloud_type.setter
    def cloud_type(self, cloud_type):
        """Sets the cloud_type of this ListBucketsReq.

        云类型 AWS：亚马逊 Aliyun：阿里云 Qiniu：七牛云 QingCloud：青云 Tencent：腾讯云 Baidu：百度云 KingsoftCloud：金山云 Azure：微软云 UCloud：优刻得 HuaweiCloud：华为云 URLSource：URL HEC：HEC

        :param cloud_type: The cloud_type of this ListBucketsReq.
        :type cloud_type: str
        """
        self._cloud_type = cloud_type

    @property
    def ak(self):
        """Gets the ak of this ListBucketsReq.

        源端桶的AK（最大长度100个字符），task_type为非url_list时，本参数为必选。

        :return: The ak of this ListBucketsReq.
        :rtype: str
        """
        return self._ak

    @ak.setter
    def ak(self, ak):
        """Sets the ak of this ListBucketsReq.

        源端桶的AK（最大长度100个字符），task_type为非url_list时，本参数为必选。

        :param ak: The ak of this ListBucketsReq.
        :type ak: str
        """
        self._ak = ak

    @property
    def sk(self):
        """Gets the sk of this ListBucketsReq.

        源端桶的SK（最大长度100个字符），task_type为非url_list时，本参数为必选。

        :return: The sk of this ListBucketsReq.
        :rtype: str
        """
        return self._sk

    @sk.setter
    def sk(self, sk):
        """Sets the sk of this ListBucketsReq.

        源端桶的SK（最大长度100个字符），task_type为非url_list时，本参数为必选。

        :param sk: The sk of this ListBucketsReq.
        :type sk: str
        """
        self._sk = sk

    @property
    def app_id(self):
        """Gets the app_id of this ListBucketsReq.

        当源端为腾讯云时，会返回此参数。

        :return: The app_id of this ListBucketsReq.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this ListBucketsReq.

        当源端为腾讯云时，会返回此参数。

        :param app_id: The app_id of this ListBucketsReq.
        :type app_id: str
        """
        self._app_id = app_id

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
        if not isinstance(other, ListBucketsReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
