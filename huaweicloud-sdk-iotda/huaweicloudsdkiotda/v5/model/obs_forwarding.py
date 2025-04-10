# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ObsForwarding:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'region_name': 'str',
        'project_id': 'str',
        'bucket_name': 'str',
        'location': 'str',
        'file_path': 'str'
    }

    attribute_map = {
        'region_name': 'region_name',
        'project_id': 'project_id',
        'bucket_name': 'bucket_name',
        'location': 'location',
        'file_path': 'file_path'
    }

    def __init__(self, region_name=None, project_id=None, bucket_name=None, location=None, file_path=None):
        r"""ObsForwarding

        The model defined in huaweicloud sdk

        :param region_name: **参数说明**：OBS服务对应的region区域
        :type region_name: str
        :param project_id: **参数说明**：OBS服务对应的projectId信息
        :type project_id: str
        :param bucket_name: **参数说明**：OBS服务对应的桶名称
        :type bucket_name: str
        :param location: **参数说明**：OBS服务对应桶的区域
        :type location: str
        :param file_path: **参数说明**：OBS服务中存储通道文件的自定义目录,多级目录可用(/)进行分隔，不可以斜杠(/)开头或结尾，不能包含两个以上相邻的斜杠(/) **取值范围**: 英文字母(a-zA-Z)、数字(0-9)、下划线(_)、中划线(-)、斜杠(/)和大括号({})，最大字符长度256个字符。其中大括号只能用于对应模板参数。 **模板参数**:    - \\{YYYY\\} 年   - \\{MM\\} 月   - \\{DD\\} 日   - \\{HH\\} 小时   - \\{appId\\} 应用ID   - \\{deviceId\\} 设备ID   例如:自定义目录结构为\\{YYYY\\}/\\{MM\\}/\\{DD\\}/\\{HH\\},则会在转发数据时，根据当前时间往对应的目录结构2021&gt;08&gt;11&gt;09下生成对应的数据。
        :type file_path: str
        """
        
        

        self._region_name = None
        self._project_id = None
        self._bucket_name = None
        self._location = None
        self._file_path = None
        self.discriminator = None

        self.region_name = region_name
        self.project_id = project_id
        self.bucket_name = bucket_name
        if location is not None:
            self.location = location
        if file_path is not None:
            self.file_path = file_path

    @property
    def region_name(self):
        r"""Gets the region_name of this ObsForwarding.

        **参数说明**：OBS服务对应的region区域

        :return: The region_name of this ObsForwarding.
        :rtype: str
        """
        return self._region_name

    @region_name.setter
    def region_name(self, region_name):
        r"""Sets the region_name of this ObsForwarding.

        **参数说明**：OBS服务对应的region区域

        :param region_name: The region_name of this ObsForwarding.
        :type region_name: str
        """
        self._region_name = region_name

    @property
    def project_id(self):
        r"""Gets the project_id of this ObsForwarding.

        **参数说明**：OBS服务对应的projectId信息

        :return: The project_id of this ObsForwarding.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ObsForwarding.

        **参数说明**：OBS服务对应的projectId信息

        :param project_id: The project_id of this ObsForwarding.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def bucket_name(self):
        r"""Gets the bucket_name of this ObsForwarding.

        **参数说明**：OBS服务对应的桶名称

        :return: The bucket_name of this ObsForwarding.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        r"""Sets the bucket_name of this ObsForwarding.

        **参数说明**：OBS服务对应的桶名称

        :param bucket_name: The bucket_name of this ObsForwarding.
        :type bucket_name: str
        """
        self._bucket_name = bucket_name

    @property
    def location(self):
        r"""Gets the location of this ObsForwarding.

        **参数说明**：OBS服务对应桶的区域

        :return: The location of this ObsForwarding.
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        r"""Sets the location of this ObsForwarding.

        **参数说明**：OBS服务对应桶的区域

        :param location: The location of this ObsForwarding.
        :type location: str
        """
        self._location = location

    @property
    def file_path(self):
        r"""Gets the file_path of this ObsForwarding.

        **参数说明**：OBS服务中存储通道文件的自定义目录,多级目录可用(/)进行分隔，不可以斜杠(/)开头或结尾，不能包含两个以上相邻的斜杠(/) **取值范围**: 英文字母(a-zA-Z)、数字(0-9)、下划线(_)、中划线(-)、斜杠(/)和大括号({})，最大字符长度256个字符。其中大括号只能用于对应模板参数。 **模板参数**:    - \\{YYYY\\} 年   - \\{MM\\} 月   - \\{DD\\} 日   - \\{HH\\} 小时   - \\{appId\\} 应用ID   - \\{deviceId\\} 设备ID   例如:自定义目录结构为\\{YYYY\\}/\\{MM\\}/\\{DD\\}/\\{HH\\},则会在转发数据时，根据当前时间往对应的目录结构2021>08>11>09下生成对应的数据。

        :return: The file_path of this ObsForwarding.
        :rtype: str
        """
        return self._file_path

    @file_path.setter
    def file_path(self, file_path):
        r"""Sets the file_path of this ObsForwarding.

        **参数说明**：OBS服务中存储通道文件的自定义目录,多级目录可用(/)进行分隔，不可以斜杠(/)开头或结尾，不能包含两个以上相邻的斜杠(/) **取值范围**: 英文字母(a-zA-Z)、数字(0-9)、下划线(_)、中划线(-)、斜杠(/)和大括号({})，最大字符长度256个字符。其中大括号只能用于对应模板参数。 **模板参数**:    - \\{YYYY\\} 年   - \\{MM\\} 月   - \\{DD\\} 日   - \\{HH\\} 小时   - \\{appId\\} 应用ID   - \\{deviceId\\} 设备ID   例如:自定义目录结构为\\{YYYY\\}/\\{MM\\}/\\{DD\\}/\\{HH\\},则会在转发数据时，根据当前时间往对应的目录结构2021>08>11>09下生成对应的数据。

        :param file_path: The file_path of this ObsForwarding.
        :type file_path: str
        """
        self._file_path = file_path

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
        if not isinstance(other, ObsForwarding):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
