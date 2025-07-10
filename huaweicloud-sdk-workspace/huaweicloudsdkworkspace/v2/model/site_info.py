# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SiteInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'site_id': 'str',
        'site_name': 'str',
        'site_type': 'str',
        'project_id': 'str',
        'status': 'str',
        'create_time': 'str'
    }

    attribute_map = {
        'site_id': 'site_id',
        'site_name': 'site_name',
        'site_type': 'site_type',
        'project_id': 'project_id',
        'status': 'status',
        'create_time': 'create_time'
    }

    def __init__(self, site_id=None, site_name=None, site_type=None, project_id=None, status=None, create_time=None):
        r"""SiteInfo

        The model defined in huaweicloud sdk

        :param site_id: 站点id。
        :type site_id: str
        :param site_name: 站点名字。
        :type site_name: str
        :param site_type: 配置状态。 - CENTER： 中心初始化 - IES： 边缘初始化
        :type site_type: str
        :param project_id: 项目ID。
        :type project_id: str
        :param status: 站点状态。
        :type status: str
        :param create_time: 创建时间。
        :type create_time: str
        """
        
        

        self._site_id = None
        self._site_name = None
        self._site_type = None
        self._project_id = None
        self._status = None
        self._create_time = None
        self.discriminator = None

        if site_id is not None:
            self.site_id = site_id
        if site_name is not None:
            self.site_name = site_name
        if site_type is not None:
            self.site_type = site_type
        if project_id is not None:
            self.project_id = project_id
        if status is not None:
            self.status = status
        if create_time is not None:
            self.create_time = create_time

    @property
    def site_id(self):
        r"""Gets the site_id of this SiteInfo.

        站点id。

        :return: The site_id of this SiteInfo.
        :rtype: str
        """
        return self._site_id

    @site_id.setter
    def site_id(self, site_id):
        r"""Sets the site_id of this SiteInfo.

        站点id。

        :param site_id: The site_id of this SiteInfo.
        :type site_id: str
        """
        self._site_id = site_id

    @property
    def site_name(self):
        r"""Gets the site_name of this SiteInfo.

        站点名字。

        :return: The site_name of this SiteInfo.
        :rtype: str
        """
        return self._site_name

    @site_name.setter
    def site_name(self, site_name):
        r"""Sets the site_name of this SiteInfo.

        站点名字。

        :param site_name: The site_name of this SiteInfo.
        :type site_name: str
        """
        self._site_name = site_name

    @property
    def site_type(self):
        r"""Gets the site_type of this SiteInfo.

        配置状态。 - CENTER： 中心初始化 - IES： 边缘初始化

        :return: The site_type of this SiteInfo.
        :rtype: str
        """
        return self._site_type

    @site_type.setter
    def site_type(self, site_type):
        r"""Sets the site_type of this SiteInfo.

        配置状态。 - CENTER： 中心初始化 - IES： 边缘初始化

        :param site_type: The site_type of this SiteInfo.
        :type site_type: str
        """
        self._site_type = site_type

    @property
    def project_id(self):
        r"""Gets the project_id of this SiteInfo.

        项目ID。

        :return: The project_id of this SiteInfo.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this SiteInfo.

        项目ID。

        :param project_id: The project_id of this SiteInfo.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def status(self):
        r"""Gets the status of this SiteInfo.

        站点状态。

        :return: The status of this SiteInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this SiteInfo.

        站点状态。

        :param status: The status of this SiteInfo.
        :type status: str
        """
        self._status = status

    @property
    def create_time(self):
        r"""Gets the create_time of this SiteInfo.

        创建时间。

        :return: The create_time of this SiteInfo.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this SiteInfo.

        创建时间。

        :param create_time: The create_time of this SiteInfo.
        :type create_time: str
        """
        self._create_time = create_time

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
        if not isinstance(other, SiteInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
