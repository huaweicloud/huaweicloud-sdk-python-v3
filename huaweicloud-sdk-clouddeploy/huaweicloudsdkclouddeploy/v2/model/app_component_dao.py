# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AppComponentDao:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'task_id': 'str',
        'app_id': 'str',
        'app_name': 'str',
        'comp_id': 'str',
        'comp_name': 'str',
        'domain_id': 'str',
        'region': 'str',
        'state': 'str'
    }

    attribute_map = {
        'task_id': 'task_id',
        'app_id': 'app_id',
        'app_name': 'app_name',
        'comp_id': 'comp_id',
        'comp_name': 'comp_name',
        'domain_id': 'domain_id',
        'region': 'region',
        'state': 'state'
    }

    def __init__(self, task_id=None, app_id=None, app_name=None, comp_id=None, comp_name=None, domain_id=None, region=None, state=None):
        """AppComponentDao

        The model defined in huaweicloud sdk

        :param task_id: 部署任务id
        :type task_id: str
        :param app_id: 应用id
        :type app_id: str
        :param app_name: 应用名称
        :type app_name: str
        :param comp_id: 组件id
        :type comp_id: str
        :param comp_name: 组件名称
        :type comp_name: str
        :param domain_id: 租户ID
        :type domain_id: str
        :param region: 局点信息
        :type region: str
        :param state: 组件是否生效，0表示初始化，1表示执行成功，已生效
        :type state: str
        """
        
        

        self._task_id = None
        self._app_id = None
        self._app_name = None
        self._comp_id = None
        self._comp_name = None
        self._domain_id = None
        self._region = None
        self._state = None
        self.discriminator = None

        if task_id is not None:
            self.task_id = task_id
        if app_id is not None:
            self.app_id = app_id
        if app_name is not None:
            self.app_name = app_name
        if comp_id is not None:
            self.comp_id = comp_id
        if comp_name is not None:
            self.comp_name = comp_name
        if domain_id is not None:
            self.domain_id = domain_id
        if region is not None:
            self.region = region
        if state is not None:
            self.state = state

    @property
    def task_id(self):
        """Gets the task_id of this AppComponentDao.

        部署任务id

        :return: The task_id of this AppComponentDao.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this AppComponentDao.

        部署任务id

        :param task_id: The task_id of this AppComponentDao.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def app_id(self):
        """Gets the app_id of this AppComponentDao.

        应用id

        :return: The app_id of this AppComponentDao.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this AppComponentDao.

        应用id

        :param app_id: The app_id of this AppComponentDao.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def app_name(self):
        """Gets the app_name of this AppComponentDao.

        应用名称

        :return: The app_name of this AppComponentDao.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        """Sets the app_name of this AppComponentDao.

        应用名称

        :param app_name: The app_name of this AppComponentDao.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def comp_id(self):
        """Gets the comp_id of this AppComponentDao.

        组件id

        :return: The comp_id of this AppComponentDao.
        :rtype: str
        """
        return self._comp_id

    @comp_id.setter
    def comp_id(self, comp_id):
        """Sets the comp_id of this AppComponentDao.

        组件id

        :param comp_id: The comp_id of this AppComponentDao.
        :type comp_id: str
        """
        self._comp_id = comp_id

    @property
    def comp_name(self):
        """Gets the comp_name of this AppComponentDao.

        组件名称

        :return: The comp_name of this AppComponentDao.
        :rtype: str
        """
        return self._comp_name

    @comp_name.setter
    def comp_name(self, comp_name):
        """Sets the comp_name of this AppComponentDao.

        组件名称

        :param comp_name: The comp_name of this AppComponentDao.
        :type comp_name: str
        """
        self._comp_name = comp_name

    @property
    def domain_id(self):
        """Gets the domain_id of this AppComponentDao.

        租户ID

        :return: The domain_id of this AppComponentDao.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this AppComponentDao.

        租户ID

        :param domain_id: The domain_id of this AppComponentDao.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def region(self):
        """Gets the region of this AppComponentDao.

        局点信息

        :return: The region of this AppComponentDao.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this AppComponentDao.

        局点信息

        :param region: The region of this AppComponentDao.
        :type region: str
        """
        self._region = region

    @property
    def state(self):
        """Gets the state of this AppComponentDao.

        组件是否生效，0表示初始化，1表示执行成功，已生效

        :return: The state of this AppComponentDao.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this AppComponentDao.

        组件是否生效，0表示初始化，1表示执行成功，已生效

        :param state: The state of this AppComponentDao.
        :type state: str
        """
        self._state = state

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
        if not isinstance(other, AppComponentDao):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
