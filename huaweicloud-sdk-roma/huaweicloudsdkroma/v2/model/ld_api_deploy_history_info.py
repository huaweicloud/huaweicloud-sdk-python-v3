# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LdApiDeployHistoryInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'ld_api_id': 'str',
        'group_id': 'str',
        'env_id': 'str',
        'api_id': 'str',
        'deploy_time': 'datetime',
        'api_definition': 'LdApiInfo'
    }

    attribute_map = {
        'id': 'id',
        'ld_api_id': 'ld_api_id',
        'group_id': 'group_id',
        'env_id': 'env_id',
        'api_id': 'api_id',
        'deploy_time': 'deploy_time',
        'api_definition': 'api_definition'
    }

    def __init__(self, id=None, ld_api_id=None, group_id=None, env_id=None, api_id=None, deploy_time=None, api_definition=None):
        """LdApiDeployHistoryInfo

        The model defined in huaweicloud sdk

        :param id: 部署的编号
        :type id: str
        :param ld_api_id: 部署的后端API编号
        :type ld_api_id: str
        :param group_id: 部署的前端API分组编号
        :type group_id: str
        :param env_id: 部署的环境编号
        :type env_id: str
        :param api_id: 部署的前端API编号
        :type api_id: str
        :param deploy_time: 部署时间
        :type deploy_time: datetime
        :param api_definition: 
        :type api_definition: :class:`huaweicloudsdkroma.v2.LdApiInfo`
        """
        
        

        self._id = None
        self._ld_api_id = None
        self._group_id = None
        self._env_id = None
        self._api_id = None
        self._deploy_time = None
        self._api_definition = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if ld_api_id is not None:
            self.ld_api_id = ld_api_id
        if group_id is not None:
            self.group_id = group_id
        if env_id is not None:
            self.env_id = env_id
        if api_id is not None:
            self.api_id = api_id
        if deploy_time is not None:
            self.deploy_time = deploy_time
        if api_definition is not None:
            self.api_definition = api_definition

    @property
    def id(self):
        """Gets the id of this LdApiDeployHistoryInfo.

        部署的编号

        :return: The id of this LdApiDeployHistoryInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LdApiDeployHistoryInfo.

        部署的编号

        :param id: The id of this LdApiDeployHistoryInfo.
        :type id: str
        """
        self._id = id

    @property
    def ld_api_id(self):
        """Gets the ld_api_id of this LdApiDeployHistoryInfo.

        部署的后端API编号

        :return: The ld_api_id of this LdApiDeployHistoryInfo.
        :rtype: str
        """
        return self._ld_api_id

    @ld_api_id.setter
    def ld_api_id(self, ld_api_id):
        """Sets the ld_api_id of this LdApiDeployHistoryInfo.

        部署的后端API编号

        :param ld_api_id: The ld_api_id of this LdApiDeployHistoryInfo.
        :type ld_api_id: str
        """
        self._ld_api_id = ld_api_id

    @property
    def group_id(self):
        """Gets the group_id of this LdApiDeployHistoryInfo.

        部署的前端API分组编号

        :return: The group_id of this LdApiDeployHistoryInfo.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this LdApiDeployHistoryInfo.

        部署的前端API分组编号

        :param group_id: The group_id of this LdApiDeployHistoryInfo.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def env_id(self):
        """Gets the env_id of this LdApiDeployHistoryInfo.

        部署的环境编号

        :return: The env_id of this LdApiDeployHistoryInfo.
        :rtype: str
        """
        return self._env_id

    @env_id.setter
    def env_id(self, env_id):
        """Sets the env_id of this LdApiDeployHistoryInfo.

        部署的环境编号

        :param env_id: The env_id of this LdApiDeployHistoryInfo.
        :type env_id: str
        """
        self._env_id = env_id

    @property
    def api_id(self):
        """Gets the api_id of this LdApiDeployHistoryInfo.

        部署的前端API编号

        :return: The api_id of this LdApiDeployHistoryInfo.
        :rtype: str
        """
        return self._api_id

    @api_id.setter
    def api_id(self, api_id):
        """Sets the api_id of this LdApiDeployHistoryInfo.

        部署的前端API编号

        :param api_id: The api_id of this LdApiDeployHistoryInfo.
        :type api_id: str
        """
        self._api_id = api_id

    @property
    def deploy_time(self):
        """Gets the deploy_time of this LdApiDeployHistoryInfo.

        部署时间

        :return: The deploy_time of this LdApiDeployHistoryInfo.
        :rtype: datetime
        """
        return self._deploy_time

    @deploy_time.setter
    def deploy_time(self, deploy_time):
        """Sets the deploy_time of this LdApiDeployHistoryInfo.

        部署时间

        :param deploy_time: The deploy_time of this LdApiDeployHistoryInfo.
        :type deploy_time: datetime
        """
        self._deploy_time = deploy_time

    @property
    def api_definition(self):
        """Gets the api_definition of this LdApiDeployHistoryInfo.


        :return: The api_definition of this LdApiDeployHistoryInfo.
        :rtype: :class:`huaweicloudsdkroma.v2.LdApiInfo`
        """
        return self._api_definition

    @api_definition.setter
    def api_definition(self, api_definition):
        """Sets the api_definition of this LdApiDeployHistoryInfo.


        :param api_definition: The api_definition of this LdApiDeployHistoryInfo.
        :type api_definition: :class:`huaweicloudsdkroma.v2.LdApiInfo`
        """
        self._api_definition = api_definition

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
        if not isinstance(other, LdApiDeployHistoryInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
