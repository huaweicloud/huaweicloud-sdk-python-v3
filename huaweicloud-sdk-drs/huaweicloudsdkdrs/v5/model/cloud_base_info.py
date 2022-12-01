# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CloudBaseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'region': 'str',
        'project_id': 'str',
        'az_code': 'str'
    }

    attribute_map = {
        'region': 'region',
        'project_id': 'project_id',
        'az_code': 'az_code'
    }

    def __init__(self, region=None, project_id=None, az_code=None):
        """CloudBaseInfo

        The model defined in huaweicloud sdk

        :param region: 区域ID，当数据库实例类型为ecs（华为云ECS自建数据库），cloud（华为云数据库）时为必填项。获取方法请参见地区和终端节点。 注意：当该Region下存在子项目时，Region ID为区域项目ID与子项目ID，由“_”下划线拼接，例如：cn-north-4_abc。
        :type region: str
        :param project_id: 租户在某一Region下的Project ID。 获取方法请参见获取项目ID。
        :type project_id: str
        :param az_code: 数据库所在可用分区（AZ）名称。
        :type az_code: str
        """
        
        

        self._region = None
        self._project_id = None
        self._az_code = None
        self.discriminator = None

        self.region = region
        self.project_id = project_id
        if az_code is not None:
            self.az_code = az_code

    @property
    def region(self):
        """Gets the region of this CloudBaseInfo.

        区域ID，当数据库实例类型为ecs（华为云ECS自建数据库），cloud（华为云数据库）时为必填项。获取方法请参见地区和终端节点。 注意：当该Region下存在子项目时，Region ID为区域项目ID与子项目ID，由“_”下划线拼接，例如：cn-north-4_abc。

        :return: The region of this CloudBaseInfo.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this CloudBaseInfo.

        区域ID，当数据库实例类型为ecs（华为云ECS自建数据库），cloud（华为云数据库）时为必填项。获取方法请参见地区和终端节点。 注意：当该Region下存在子项目时，Region ID为区域项目ID与子项目ID，由“_”下划线拼接，例如：cn-north-4_abc。

        :param region: The region of this CloudBaseInfo.
        :type region: str
        """
        self._region = region

    @property
    def project_id(self):
        """Gets the project_id of this CloudBaseInfo.

        租户在某一Region下的Project ID。 获取方法请参见获取项目ID。

        :return: The project_id of this CloudBaseInfo.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this CloudBaseInfo.

        租户在某一Region下的Project ID。 获取方法请参见获取项目ID。

        :param project_id: The project_id of this CloudBaseInfo.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def az_code(self):
        """Gets the az_code of this CloudBaseInfo.

        数据库所在可用分区（AZ）名称。

        :return: The az_code of this CloudBaseInfo.
        :rtype: str
        """
        return self._az_code

    @az_code.setter
    def az_code(self, az_code):
        """Sets the az_code of this CloudBaseInfo.

        数据库所在可用分区（AZ）名称。

        :param az_code: The az_code of this CloudBaseInfo.
        :type az_code: str
        """
        self._az_code = az_code

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
        if not isinstance(other, CloudBaseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
