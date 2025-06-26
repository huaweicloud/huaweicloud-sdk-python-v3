# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateSimBatchesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'url': 'str',
        'id': 'int',
        'created_at': 'float',
        'updated_at': 'float',
        'passing_score': 'int',
        'algorithm_name': 'str',
        'algorithm_image': 'str',
        'algorithm_image_version': 'str',
        'started_at': 'float',
        'ended_at': 'float',
        'success': 'int',
        'fail': 'int',
        'simulation_size': 'int',
        'status': 'int',
        'name': 'str',
        'description': 'str',
        'user_id': 'str',
        'designated_simulation_ids': 'list[int]',
        'batch_config': 'str'
    }

    attribute_map = {
        'url': 'url',
        'id': 'id',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'passing_score': 'passing_score',
        'algorithm_name': 'algorithm_name',
        'algorithm_image': 'algorithm_image',
        'algorithm_image_version': 'algorithm_image_version',
        'started_at': 'started_at',
        'ended_at': 'ended_at',
        'success': 'success',
        'fail': 'fail',
        'simulation_size': 'simulation_size',
        'status': 'status',
        'name': 'name',
        'description': 'description',
        'user_id': 'user_id',
        'designated_simulation_ids': 'designated_simulation_ids',
        'batch_config': 'batch_config'
    }

    def __init__(self, url=None, id=None, created_at=None, updated_at=None, passing_score=None, algorithm_name=None, algorithm_image=None, algorithm_image_version=None, started_at=None, ended_at=None, success=None, fail=None, simulation_size=None, status=None, name=None, description=None, user_id=None, designated_simulation_ids=None, batch_config=None):
        r"""CreateSimBatchesResponse

        The model defined in huaweicloud sdk

        :param url: 
        :type url: str
        :param id: 
        :type id: int
        :param created_at: 
        :type created_at: float
        :param updated_at: 
        :type updated_at: float
        :param passing_score: 融合评测通过分数
        :type passing_score: int
        :param algorithm_name: 关联算法名称
        :type algorithm_name: str
        :param algorithm_image: 关联算法镜像
        :type algorithm_image: str
        :param algorithm_image_version: 关联算法镜像版本
        :type algorithm_image_version: str
        :param started_at: 任务开始时间
        :type started_at: float
        :param ended_at: 任务结束时间
        :type ended_at: float
        :param success: 子任务成功数量
        :type success: int
        :param fail: 子任务失败数量
        :type fail: int
        :param simulation_size: 子任务数量
        :type simulation_size: int
        :param status: 任务状态
        :type status: int
        :param name: 名称
        :type name: str
        :param description: 文本描述
        :type description: str
        :param user_id: 用户id
        :type user_id: str
        :param designated_simulation_ids: 用户指定重跑子任务ids
        :type designated_simulation_ids: list[int]
        :param batch_config: 关联batch配置
        :type batch_config: str
        """
        
        super(CreateSimBatchesResponse, self).__init__()

        self._url = None
        self._id = None
        self._created_at = None
        self._updated_at = None
        self._passing_score = None
        self._algorithm_name = None
        self._algorithm_image = None
        self._algorithm_image_version = None
        self._started_at = None
        self._ended_at = None
        self._success = None
        self._fail = None
        self._simulation_size = None
        self._status = None
        self._name = None
        self._description = None
        self._user_id = None
        self._designated_simulation_ids = None
        self._batch_config = None
        self.discriminator = None

        if url is not None:
            self.url = url
        if id is not None:
            self.id = id
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if passing_score is not None:
            self.passing_score = passing_score
        if algorithm_name is not None:
            self.algorithm_name = algorithm_name
        self.algorithm_image = algorithm_image
        if algorithm_image_version is not None:
            self.algorithm_image_version = algorithm_image_version
        if started_at is not None:
            self.started_at = started_at
        if ended_at is not None:
            self.ended_at = ended_at
        if success is not None:
            self.success = success
        if fail is not None:
            self.fail = fail
        if simulation_size is not None:
            self.simulation_size = simulation_size
        if status is not None:
            self.status = status
        if name is not None:
            self.name = name
        self.description = description
        if user_id is not None:
            self.user_id = user_id
        self.designated_simulation_ids = designated_simulation_ids
        if batch_config is not None:
            self.batch_config = batch_config

    @property
    def url(self):
        r"""Gets the url of this CreateSimBatchesResponse.

        :return: The url of this CreateSimBatchesResponse.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this CreateSimBatchesResponse.

        :param url: The url of this CreateSimBatchesResponse.
        :type url: str
        """
        self._url = url

    @property
    def id(self):
        r"""Gets the id of this CreateSimBatchesResponse.

        :return: The id of this CreateSimBatchesResponse.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CreateSimBatchesResponse.

        :param id: The id of this CreateSimBatchesResponse.
        :type id: int
        """
        self._id = id

    @property
    def created_at(self):
        r"""Gets the created_at of this CreateSimBatchesResponse.

        :return: The created_at of this CreateSimBatchesResponse.
        :rtype: float
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this CreateSimBatchesResponse.

        :param created_at: The created_at of this CreateSimBatchesResponse.
        :type created_at: float
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this CreateSimBatchesResponse.

        :return: The updated_at of this CreateSimBatchesResponse.
        :rtype: float
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this CreateSimBatchesResponse.

        :param updated_at: The updated_at of this CreateSimBatchesResponse.
        :type updated_at: float
        """
        self._updated_at = updated_at

    @property
    def passing_score(self):
        r"""Gets the passing_score of this CreateSimBatchesResponse.

        融合评测通过分数

        :return: The passing_score of this CreateSimBatchesResponse.
        :rtype: int
        """
        return self._passing_score

    @passing_score.setter
    def passing_score(self, passing_score):
        r"""Sets the passing_score of this CreateSimBatchesResponse.

        融合评测通过分数

        :param passing_score: The passing_score of this CreateSimBatchesResponse.
        :type passing_score: int
        """
        self._passing_score = passing_score

    @property
    def algorithm_name(self):
        r"""Gets the algorithm_name of this CreateSimBatchesResponse.

        关联算法名称

        :return: The algorithm_name of this CreateSimBatchesResponse.
        :rtype: str
        """
        return self._algorithm_name

    @algorithm_name.setter
    def algorithm_name(self, algorithm_name):
        r"""Sets the algorithm_name of this CreateSimBatchesResponse.

        关联算法名称

        :param algorithm_name: The algorithm_name of this CreateSimBatchesResponse.
        :type algorithm_name: str
        """
        self._algorithm_name = algorithm_name

    @property
    def algorithm_image(self):
        r"""Gets the algorithm_image of this CreateSimBatchesResponse.

        关联算法镜像

        :return: The algorithm_image of this CreateSimBatchesResponse.
        :rtype: str
        """
        return self._algorithm_image

    @algorithm_image.setter
    def algorithm_image(self, algorithm_image):
        r"""Sets the algorithm_image of this CreateSimBatchesResponse.

        关联算法镜像

        :param algorithm_image: The algorithm_image of this CreateSimBatchesResponse.
        :type algorithm_image: str
        """
        self._algorithm_image = algorithm_image

    @property
    def algorithm_image_version(self):
        r"""Gets the algorithm_image_version of this CreateSimBatchesResponse.

        关联算法镜像版本

        :return: The algorithm_image_version of this CreateSimBatchesResponse.
        :rtype: str
        """
        return self._algorithm_image_version

    @algorithm_image_version.setter
    def algorithm_image_version(self, algorithm_image_version):
        r"""Sets the algorithm_image_version of this CreateSimBatchesResponse.

        关联算法镜像版本

        :param algorithm_image_version: The algorithm_image_version of this CreateSimBatchesResponse.
        :type algorithm_image_version: str
        """
        self._algorithm_image_version = algorithm_image_version

    @property
    def started_at(self):
        r"""Gets the started_at of this CreateSimBatchesResponse.

        任务开始时间

        :return: The started_at of this CreateSimBatchesResponse.
        :rtype: float
        """
        return self._started_at

    @started_at.setter
    def started_at(self, started_at):
        r"""Sets the started_at of this CreateSimBatchesResponse.

        任务开始时间

        :param started_at: The started_at of this CreateSimBatchesResponse.
        :type started_at: float
        """
        self._started_at = started_at

    @property
    def ended_at(self):
        r"""Gets the ended_at of this CreateSimBatchesResponse.

        任务结束时间

        :return: The ended_at of this CreateSimBatchesResponse.
        :rtype: float
        """
        return self._ended_at

    @ended_at.setter
    def ended_at(self, ended_at):
        r"""Sets the ended_at of this CreateSimBatchesResponse.

        任务结束时间

        :param ended_at: The ended_at of this CreateSimBatchesResponse.
        :type ended_at: float
        """
        self._ended_at = ended_at

    @property
    def success(self):
        r"""Gets the success of this CreateSimBatchesResponse.

        子任务成功数量

        :return: The success of this CreateSimBatchesResponse.
        :rtype: int
        """
        return self._success

    @success.setter
    def success(self, success):
        r"""Sets the success of this CreateSimBatchesResponse.

        子任务成功数量

        :param success: The success of this CreateSimBatchesResponse.
        :type success: int
        """
        self._success = success

    @property
    def fail(self):
        r"""Gets the fail of this CreateSimBatchesResponse.

        子任务失败数量

        :return: The fail of this CreateSimBatchesResponse.
        :rtype: int
        """
        return self._fail

    @fail.setter
    def fail(self, fail):
        r"""Sets the fail of this CreateSimBatchesResponse.

        子任务失败数量

        :param fail: The fail of this CreateSimBatchesResponse.
        :type fail: int
        """
        self._fail = fail

    @property
    def simulation_size(self):
        r"""Gets the simulation_size of this CreateSimBatchesResponse.

        子任务数量

        :return: The simulation_size of this CreateSimBatchesResponse.
        :rtype: int
        """
        return self._simulation_size

    @simulation_size.setter
    def simulation_size(self, simulation_size):
        r"""Sets the simulation_size of this CreateSimBatchesResponse.

        子任务数量

        :param simulation_size: The simulation_size of this CreateSimBatchesResponse.
        :type simulation_size: int
        """
        self._simulation_size = simulation_size

    @property
    def status(self):
        r"""Gets the status of this CreateSimBatchesResponse.

        任务状态

        :return: The status of this CreateSimBatchesResponse.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this CreateSimBatchesResponse.

        任务状态

        :param status: The status of this CreateSimBatchesResponse.
        :type status: int
        """
        self._status = status

    @property
    def name(self):
        r"""Gets the name of this CreateSimBatchesResponse.

        名称

        :return: The name of this CreateSimBatchesResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateSimBatchesResponse.

        名称

        :param name: The name of this CreateSimBatchesResponse.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this CreateSimBatchesResponse.

        文本描述

        :return: The description of this CreateSimBatchesResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateSimBatchesResponse.

        文本描述

        :param description: The description of this CreateSimBatchesResponse.
        :type description: str
        """
        self._description = description

    @property
    def user_id(self):
        r"""Gets the user_id of this CreateSimBatchesResponse.

        用户id

        :return: The user_id of this CreateSimBatchesResponse.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this CreateSimBatchesResponse.

        用户id

        :param user_id: The user_id of this CreateSimBatchesResponse.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def designated_simulation_ids(self):
        r"""Gets the designated_simulation_ids of this CreateSimBatchesResponse.

        用户指定重跑子任务ids

        :return: The designated_simulation_ids of this CreateSimBatchesResponse.
        :rtype: list[int]
        """
        return self._designated_simulation_ids

    @designated_simulation_ids.setter
    def designated_simulation_ids(self, designated_simulation_ids):
        r"""Sets the designated_simulation_ids of this CreateSimBatchesResponse.

        用户指定重跑子任务ids

        :param designated_simulation_ids: The designated_simulation_ids of this CreateSimBatchesResponse.
        :type designated_simulation_ids: list[int]
        """
        self._designated_simulation_ids = designated_simulation_ids

    @property
    def batch_config(self):
        r"""Gets the batch_config of this CreateSimBatchesResponse.

        关联batch配置

        :return: The batch_config of this CreateSimBatchesResponse.
        :rtype: str
        """
        return self._batch_config

    @batch_config.setter
    def batch_config(self, batch_config):
        r"""Sets the batch_config of this CreateSimBatchesResponse.

        关联batch配置

        :param batch_config: The batch_config of this CreateSimBatchesResponse.
        :type batch_config: str
        """
        self._batch_config = batch_config

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
        if not isinstance(other, CreateSimBatchesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
