# coding: utf-8

import pprint
import re

import six





class CreateBatchTask:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'app_id': 'str',
        'task_name': 'str',
        'task_type': 'str',
        'targets': 'list[str]',
        'targets_filter': 'dict(str, object)',
        'document': 'object',
        'task_policy': 'TaskPolicy',
        'document_source': 'str'
    }

    attribute_map = {
        'app_id': 'app_id',
        'task_name': 'task_name',
        'task_type': 'task_type',
        'targets': 'targets',
        'targets_filter': 'targets_filter',
        'document': 'document',
        'task_policy': 'task_policy',
        'document_source': 'document_source'
    }

    def __init__(self, app_id=None, task_name=None, task_type=None, targets=None, targets_filter=None, document=None, task_policy=None, document_source=None):
        """CreateBatchTask - a model defined in huaweicloud sdk"""
        
        

        self._app_id = None
        self._task_name = None
        self._task_type = None
        self._targets = None
        self._targets_filter = None
        self._document = None
        self._task_policy = None
        self._document_source = None
        self.discriminator = None

        if app_id is not None:
            self.app_id = app_id
        self.task_name = task_name
        self.task_type = task_type
        if targets is not None:
            self.targets = targets
        if targets_filter is not None:
            self.targets_filter = targets_filter
        if document is not None:
            self.document = document
        if task_policy is not None:
            self.task_policy = task_policy
        if document_source is not None:
            self.document_source = document_source

    @property
    def app_id(self):
        """Gets the app_id of this CreateBatchTask.

        资源空间ID。此参数为非必选参数，存在多资源空间的用户需要使用该接口时，建议携带该参数指定创建的批量任务归属到哪个资源空间下，否则创建的批量任务将会归属到[默认资源空间](https://support.huaweicloud.com/usermanual-iothub/iot_01_0006.html#section0)下。

        :return: The app_id of this CreateBatchTask.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this CreateBatchTask.

        资源空间ID。此参数为非必选参数，存在多资源空间的用户需要使用该接口时，建议携带该参数指定创建的批量任务归属到哪个资源空间下，否则创建的批量任务将会归属到[默认资源空间](https://support.huaweicloud.com/usermanual-iothub/iot_01_0006.html#section0)下。

        :param app_id: The app_id of this CreateBatchTask.
        :type: str
        """
        self._app_id = app_id

    @property
    def task_name(self):
        """Gets the task_name of this CreateBatchTask.

        批量任务名称。

        :return: The task_name of this CreateBatchTask.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        """Sets the task_name of this CreateBatchTask.

        批量任务名称。

        :param task_name: The task_name of this CreateBatchTask.
        :type: str
        """
        self._task_name = task_name

    @property
    def task_type(self):
        """Gets the task_type of this CreateBatchTask.

        批量任务类型，取值范围：firmwareUpgrade，softwareUpgrade。 - softwareUpgrade: 软件升级任务 - firmwareUpgrade: 固件升级任务 

        :return: The task_type of this CreateBatchTask.
        :rtype: str
        """
        return self._task_type

    @task_type.setter
    def task_type(self, task_type):
        """Sets the task_type of this CreateBatchTask.

        批量任务类型，取值范围：firmwareUpgrade，softwareUpgrade。 - softwareUpgrade: 软件升级任务 - firmwareUpgrade: 固件升级任务 

        :param task_type: The task_type of this CreateBatchTask.
        :type: str
        """
        self._task_type = task_type

    @property
    def targets(self):
        """Gets the targets of this CreateBatchTask.

        执行批量任务的目标，当task_type为firmwareUpgrade，softwareUpgrade时，此处填写device_id列表。

        :return: The targets of this CreateBatchTask.
        :rtype: list[str]
        """
        return self._targets

    @targets.setter
    def targets(self, targets):
        """Sets the targets of this CreateBatchTask.

        执行批量任务的目标，当task_type为firmwareUpgrade，softwareUpgrade时，此处填写device_id列表。

        :param targets: The targets of this CreateBatchTask.
        :type: list[str]
        """
        self._targets = targets

    @property
    def targets_filter(self):
        """Gets the targets_filter of this CreateBatchTask.

        任务目标筛选参数。Json格式，里面是一个个键值对，（K,V）格式标识筛选targets需要的参数，目前支持的K有group_ids（V填写group_id数组，eg:[\"e495cf17-ff79-4294-8f64-4d367919d665\"]，任务则会筛选出来符合该群组条件的设备作为目标）

        :return: The targets_filter of this CreateBatchTask.
        :rtype: dict(str, object)
        """
        return self._targets_filter

    @targets_filter.setter
    def targets_filter(self, targets_filter):
        """Sets the targets_filter of this CreateBatchTask.

        任务目标筛选参数。Json格式，里面是一个个键值对，（K,V）格式标识筛选targets需要的参数，目前支持的K有group_ids（V填写group_id数组，eg:[\"e495cf17-ff79-4294-8f64-4d367919d665\"]，任务则会筛选出来符合该群组条件的设备作为目标）

        :param targets_filter: The targets_filter of this CreateBatchTask.
        :type: dict(str, object)
        """
        self._targets_filter = targets_filter

    @property
    def document(self):
        """Gets the document of this CreateBatchTask.

        执行任务数据文档，Json格式，里面是(K,V)键值对。(当task_type 为softwareUpgrade|firmwareUpgrade，也就是软固件升级任务时需要填写key为package_id，value为在平台上传的软固件附件id，id由portal软件库包管理上传并查询获得)。

        :return: The document of this CreateBatchTask.
        :rtype: object
        """
        return self._document

    @document.setter
    def document(self, document):
        """Sets the document of this CreateBatchTask.

        执行任务数据文档，Json格式，里面是(K,V)键值对。(当task_type 为softwareUpgrade|firmwareUpgrade，也就是软固件升级任务时需要填写key为package_id，value为在平台上传的软固件附件id，id由portal软件库包管理上传并查询获得)。

        :param document: The document of this CreateBatchTask.
        :type: object
        """
        self._document = document

    @property
    def task_policy(self):
        """Gets the task_policy of this CreateBatchTask.


        :return: The task_policy of this CreateBatchTask.
        :rtype: TaskPolicy
        """
        return self._task_policy

    @task_policy.setter
    def task_policy(self, task_policy):
        """Sets the task_policy of this CreateBatchTask.


        :param task_policy: The task_policy of this CreateBatchTask.
        :type: TaskPolicy
        """
        self._task_policy = task_policy

    @property
    def document_source(self):
        """Gets the document_source of this CreateBatchTask.

        上传的批量任务文件ID。

        :return: The document_source of this CreateBatchTask.
        :rtype: str
        """
        return self._document_source

    @document_source.setter
    def document_source(self, document_source):
        """Sets the document_source of this CreateBatchTask.

        上传的批量任务文件ID。

        :param document_source: The document_source of this CreateBatchTask.
        :type: str
        """
        self._document_source = document_source

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CreateBatchTask):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
