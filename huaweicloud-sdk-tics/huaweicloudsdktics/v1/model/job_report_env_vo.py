# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JobReportEnvVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'agg_name': 'str',
        'league_id': 'str',
        'league_name': 'str',
        'project_id': 'str',
        'region_id': 'str'
    }

    attribute_map = {
        'agg_name': 'agg_name',
        'league_id': 'league_id',
        'league_name': 'league_name',
        'project_id': 'project_id',
        'region_id': 'region_id'
    }

    def __init__(self, agg_name=None, league_id=None, league_name=None, project_id=None, region_id=None):
        """JobReportEnvVo

        The model defined in huaweicloud sdk

        :param agg_name: 聚合器名称
        :type agg_name: str
        :param league_id: 联盟id
        :type league_id: str
        :param league_name: 联盟名称
        :type league_name: str
        :param project_id: 项目id
        :type project_id: str
        :param region_id: 区域
        :type region_id: str
        """
        
        

        self._agg_name = None
        self._league_id = None
        self._league_name = None
        self._project_id = None
        self._region_id = None
        self.discriminator = None

        if agg_name is not None:
            self.agg_name = agg_name
        if league_id is not None:
            self.league_id = league_id
        if league_name is not None:
            self.league_name = league_name
        if project_id is not None:
            self.project_id = project_id
        if region_id is not None:
            self.region_id = region_id

    @property
    def agg_name(self):
        """Gets the agg_name of this JobReportEnvVo.

        聚合器名称

        :return: The agg_name of this JobReportEnvVo.
        :rtype: str
        """
        return self._agg_name

    @agg_name.setter
    def agg_name(self, agg_name):
        """Sets the agg_name of this JobReportEnvVo.

        聚合器名称

        :param agg_name: The agg_name of this JobReportEnvVo.
        :type agg_name: str
        """
        self._agg_name = agg_name

    @property
    def league_id(self):
        """Gets the league_id of this JobReportEnvVo.

        联盟id

        :return: The league_id of this JobReportEnvVo.
        :rtype: str
        """
        return self._league_id

    @league_id.setter
    def league_id(self, league_id):
        """Sets the league_id of this JobReportEnvVo.

        联盟id

        :param league_id: The league_id of this JobReportEnvVo.
        :type league_id: str
        """
        self._league_id = league_id

    @property
    def league_name(self):
        """Gets the league_name of this JobReportEnvVo.

        联盟名称

        :return: The league_name of this JobReportEnvVo.
        :rtype: str
        """
        return self._league_name

    @league_name.setter
    def league_name(self, league_name):
        """Sets the league_name of this JobReportEnvVo.

        联盟名称

        :param league_name: The league_name of this JobReportEnvVo.
        :type league_name: str
        """
        self._league_name = league_name

    @property
    def project_id(self):
        """Gets the project_id of this JobReportEnvVo.

        项目id

        :return: The project_id of this JobReportEnvVo.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this JobReportEnvVo.

        项目id

        :param project_id: The project_id of this JobReportEnvVo.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def region_id(self):
        """Gets the region_id of this JobReportEnvVo.

        区域

        :return: The region_id of this JobReportEnvVo.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this JobReportEnvVo.

        区域

        :param region_id: The region_id of this JobReportEnvVo.
        :type region_id: str
        """
        self._region_id = region_id

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
        if not isinstance(other, JobReportEnvVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
