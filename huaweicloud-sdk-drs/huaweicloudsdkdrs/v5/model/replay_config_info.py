# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ReplayConfigInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'db_instance_id': 'str',
        'cloud_type': 'str',
        'ak': 'str',
        'sk': 'str',
        'db_source': 'str',
        'region': 'str',
        'traffic_source': 'str'
    }

    attribute_map = {
        'db_instance_id': 'db_instance_id',
        'cloud_type': 'cloud_type',
        'ak': 'ak',
        'sk': 'sk',
        'db_source': 'db_source',
        'region': 'region',
        'traffic_source': 'traffic_source'
    }

    def __init__(self, db_instance_id=None, cloud_type=None, ak=None, sk=None, db_source=None, region=None, traffic_source=None):
        r"""ReplayConfigInfo

        The model defined in huaweicloud sdk

        :param db_instance_id: 源实例ID。
        :type db_instance_id: str
        :param cloud_type: 云类型： - AWSCloud：亚马逊云。 - TencentCloud：腾讯云。 - AliCloud：阿里云。
        :type cloud_type: str
        :param ak: 其他云AK信息。
        :type ak: str
        :param sk: 其他云SK信息。
        :type sk: str
        :param db_source: 源数据库来源。取值： - aws_aurora_mysql：Amazon Aurora MySQL。 - tencent_tdsql_c：腾讯云TDSQL-C MySQL。 - ali_rds_mysql：阿里云RDS MySQL。
        :type db_source: str
        :param region: 其他云Region名称。
        :type region: str
        :param traffic_source: 流量文件来源。 - sdk：通过三方云API接口方式下载审计日志。
        :type traffic_source: str
        """
        
        

        self._db_instance_id = None
        self._cloud_type = None
        self._ak = None
        self._sk = None
        self._db_source = None
        self._region = None
        self._traffic_source = None
        self.discriminator = None

        self.db_instance_id = db_instance_id
        self.cloud_type = cloud_type
        self.ak = ak
        self.sk = sk
        self.db_source = db_source
        self.region = region
        self.traffic_source = traffic_source

    @property
    def db_instance_id(self):
        r"""Gets the db_instance_id of this ReplayConfigInfo.

        源实例ID。

        :return: The db_instance_id of this ReplayConfigInfo.
        :rtype: str
        """
        return self._db_instance_id

    @db_instance_id.setter
    def db_instance_id(self, db_instance_id):
        r"""Sets the db_instance_id of this ReplayConfigInfo.

        源实例ID。

        :param db_instance_id: The db_instance_id of this ReplayConfigInfo.
        :type db_instance_id: str
        """
        self._db_instance_id = db_instance_id

    @property
    def cloud_type(self):
        r"""Gets the cloud_type of this ReplayConfigInfo.

        云类型： - AWSCloud：亚马逊云。 - TencentCloud：腾讯云。 - AliCloud：阿里云。

        :return: The cloud_type of this ReplayConfigInfo.
        :rtype: str
        """
        return self._cloud_type

    @cloud_type.setter
    def cloud_type(self, cloud_type):
        r"""Sets the cloud_type of this ReplayConfigInfo.

        云类型： - AWSCloud：亚马逊云。 - TencentCloud：腾讯云。 - AliCloud：阿里云。

        :param cloud_type: The cloud_type of this ReplayConfigInfo.
        :type cloud_type: str
        """
        self._cloud_type = cloud_type

    @property
    def ak(self):
        r"""Gets the ak of this ReplayConfigInfo.

        其他云AK信息。

        :return: The ak of this ReplayConfigInfo.
        :rtype: str
        """
        return self._ak

    @ak.setter
    def ak(self, ak):
        r"""Sets the ak of this ReplayConfigInfo.

        其他云AK信息。

        :param ak: The ak of this ReplayConfigInfo.
        :type ak: str
        """
        self._ak = ak

    @property
    def sk(self):
        r"""Gets the sk of this ReplayConfigInfo.

        其他云SK信息。

        :return: The sk of this ReplayConfigInfo.
        :rtype: str
        """
        return self._sk

    @sk.setter
    def sk(self, sk):
        r"""Sets the sk of this ReplayConfigInfo.

        其他云SK信息。

        :param sk: The sk of this ReplayConfigInfo.
        :type sk: str
        """
        self._sk = sk

    @property
    def db_source(self):
        r"""Gets the db_source of this ReplayConfigInfo.

        源数据库来源。取值： - aws_aurora_mysql：Amazon Aurora MySQL。 - tencent_tdsql_c：腾讯云TDSQL-C MySQL。 - ali_rds_mysql：阿里云RDS MySQL。

        :return: The db_source of this ReplayConfigInfo.
        :rtype: str
        """
        return self._db_source

    @db_source.setter
    def db_source(self, db_source):
        r"""Sets the db_source of this ReplayConfigInfo.

        源数据库来源。取值： - aws_aurora_mysql：Amazon Aurora MySQL。 - tencent_tdsql_c：腾讯云TDSQL-C MySQL。 - ali_rds_mysql：阿里云RDS MySQL。

        :param db_source: The db_source of this ReplayConfigInfo.
        :type db_source: str
        """
        self._db_source = db_source

    @property
    def region(self):
        r"""Gets the region of this ReplayConfigInfo.

        其他云Region名称。

        :return: The region of this ReplayConfigInfo.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this ReplayConfigInfo.

        其他云Region名称。

        :param region: The region of this ReplayConfigInfo.
        :type region: str
        """
        self._region = region

    @property
    def traffic_source(self):
        r"""Gets the traffic_source of this ReplayConfigInfo.

        流量文件来源。 - sdk：通过三方云API接口方式下载审计日志。

        :return: The traffic_source of this ReplayConfigInfo.
        :rtype: str
        """
        return self._traffic_source

    @traffic_source.setter
    def traffic_source(self, traffic_source):
        r"""Sets the traffic_source of this ReplayConfigInfo.

        流量文件来源。 - sdk：通过三方云API接口方式下载审计日志。

        :param traffic_source: The traffic_source of this ReplayConfigInfo.
        :type traffic_source: str
        """
        self._traffic_source = traffic_source

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
        if not isinstance(other, ReplayConfigInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
