# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JobConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'nearline_recall_param': 'NearLineRecallParam',
        'max_recommended_num': 'int',
        'match_feature_pairs': 'list[MatchFeaturePair]',
        'striping': 'Striping',
        'match_type': 'str',
        'matrix_factorization': 'MatrixFactorization',
        'behavior_frequencys': 'list[BehaviorFrequency]',
        'file_path': 'str',
        'ucb_param': 'UcbParam',
        'behavior_gravity': 'BehaviorGravity',
        'category': 'Category',
        'behavior_logic': 'str',
        'features_engineering': 'EtlBasicParameter',
        'sample_param': 'SampleParam',
        'deep_learning_parameters': 'DeepLearingParam',
        'algorithm_specify_parameters': 'AlgorithmSpecifyParameters',
        'load_widetable': 'bool',
        'load_profile': 'bool',
        'save_mode': 'str',
        'indicators': 'list[Indicator]',
        'offline_rank_job_name': 'str',
        'update_interval': 'int',
        'optimizer': 'Optimizer',
        'flows': 'Flow'
    }

    attribute_map = {
        'nearline_recall_param': 'nearline_recall_param',
        'max_recommended_num': 'max_recommended_num',
        'match_feature_pairs': 'match_feature_pairs',
        'striping': 'striping',
        'match_type': 'match_type',
        'matrix_factorization': 'matrix_factorization',
        'behavior_frequencys': 'behavior_frequencys',
        'file_path': 'file_path',
        'ucb_param': 'ucb_param',
        'behavior_gravity': 'behavior_gravity',
        'category': 'category',
        'behavior_logic': 'behavior_logic',
        'features_engineering': 'features_engineering',
        'sample_param': 'sample_param',
        'deep_learning_parameters': 'deep_learning_parameters',
        'algorithm_specify_parameters': 'algorithm_specify_parameters',
        'load_widetable': 'load_widetable',
        'load_profile': 'load_profile',
        'save_mode': 'save_mode',
        'indicators': 'indicators',
        'offline_rank_job_name': 'offline_rank_job_name',
        'update_interval': 'update_interval',
        'optimizer': 'optimizer',
        'flows': 'flows'
    }

    def __init__(self, nearline_recall_param=None, max_recommended_num=None, match_feature_pairs=None, striping=None, match_type=None, matrix_factorization=None, behavior_frequencys=None, file_path=None, ucb_param=None, behavior_gravity=None, category=None, behavior_logic=None, features_engineering=None, sample_param=None, deep_learning_parameters=None, algorithm_specify_parameters=None, load_widetable=None, load_profile=None, save_mode=None, indicators=None, offline_rank_job_name=None, update_interval=None, optimizer=None, flows=None):
        r"""JobConfig

        The model defined in huaweicloud sdk

        :param nearline_recall_param: 
        :type nearline_recall_param: :class:`huaweicloudsdkres.v1.NearLineRecallParam`
        :param max_recommended_num: 最大候选集个数（所有召回作业需提供此参数）。
        :type max_recommended_num: int
        :param match_feature_pairs: 匹配特征对（属性匹配召回作业需要提供此参数）。
        :type match_feature_pairs: list[:class:`huaweicloudsdkres.v1.MatchFeaturePair`]
        :param striping: 
        :type striping: :class:`huaweicloudsdkres.v1.Striping`
        :param match_type: 匹配类型（属性匹配召回作业需提供此参数）： - UI，基于用户推荐物品 - UU，基于用户推荐用户 - II，基于物品推荐物品 - IU，基于物品推荐用户
        :type match_type: str
        :param matrix_factorization: 
        :type matrix_factorization: :class:`huaweicloudsdkres.v1.MatrixFactorization`
        :param behavior_frequencys: 行为频率信息（历史行为记忆召回作业、历史行为过滤作业需提供此参数）。
        :type behavior_frequencys: list[:class:`huaweicloudsdkres.v1.BehaviorFrequency`]
        :param file_path: 文件路径（人工配置候选集作业需要提供此参数）。
        :type file_path: str
        :param ucb_param: 
        :type ucb_param: :class:`huaweicloudsdkres.v1.UcbParam`
        :param behavior_gravity: 
        :type behavior_gravity: :class:`huaweicloudsdkres.v1.BehaviorGravity`
        :param category: 
        :type category: :class:`huaweicloudsdkres.v1.Category`
        :param behavior_logic: 行为逻辑过滤（历史行为过滤作业需提供此参数）： - AND，同时满足则过滤 - OR， 满足一个则过滤
        :type behavior_logic: str
        :param features_engineering: 
        :type features_engineering: :class:`huaweicloudsdkres.v1.EtlBasicParameter`
        :param sample_param: 
        :type sample_param: :class:`huaweicloudsdkres.v1.SampleParam`
        :param deep_learning_parameters: 
        :type deep_learning_parameters: :class:`huaweicloudsdkres.v1.DeepLearingParam`
        :param algorithm_specify_parameters: 
        :type algorithm_specify_parameters: :class:`huaweicloudsdkres.v1.AlgorithmSpecifyParameters`
        :param load_widetable: 导入宽表（离线数据导入作业需要提供此参数）。
        :type load_widetable: bool
        :param load_profile: 导入画像（离线数据导入作业需要提供此参数）。
        :type load_profile: bool
        :param save_mode: 保留已有宽表（离线数据导入作业需要提供此参数）： - append，是 - new，否 - overwirte，覆盖
        :type save_mode: str
        :param indicators: 统计指标（效果评估作业需要提供此参数）。
        :type indicators: list[:class:`huaweicloudsdkres.v1.Indicator`]
        :param offline_rank_job_name: 离线排序作业名称（在线训练任务需要提供此参数）。
        :type offline_rank_job_name: str
        :param update_interval: 更新周期（在线训练任务需要提供此参数）。
        :type update_interval: int
        :param optimizer: 
        :type optimizer: :class:`huaweicloudsdkres.v1.Optimizer`
        :param flows: 
        :type flows: :class:`huaweicloudsdkres.v1.Flow`
        """
        
        

        self._nearline_recall_param = None
        self._max_recommended_num = None
        self._match_feature_pairs = None
        self._striping = None
        self._match_type = None
        self._matrix_factorization = None
        self._behavior_frequencys = None
        self._file_path = None
        self._ucb_param = None
        self._behavior_gravity = None
        self._category = None
        self._behavior_logic = None
        self._features_engineering = None
        self._sample_param = None
        self._deep_learning_parameters = None
        self._algorithm_specify_parameters = None
        self._load_widetable = None
        self._load_profile = None
        self._save_mode = None
        self._indicators = None
        self._offline_rank_job_name = None
        self._update_interval = None
        self._optimizer = None
        self._flows = None
        self.discriminator = None

        if nearline_recall_param is not None:
            self.nearline_recall_param = nearline_recall_param
        if max_recommended_num is not None:
            self.max_recommended_num = max_recommended_num
        if match_feature_pairs is not None:
            self.match_feature_pairs = match_feature_pairs
        if striping is not None:
            self.striping = striping
        if match_type is not None:
            self.match_type = match_type
        if matrix_factorization is not None:
            self.matrix_factorization = matrix_factorization
        if behavior_frequencys is not None:
            self.behavior_frequencys = behavior_frequencys
        if file_path is not None:
            self.file_path = file_path
        if ucb_param is not None:
            self.ucb_param = ucb_param
        if behavior_gravity is not None:
            self.behavior_gravity = behavior_gravity
        if category is not None:
            self.category = category
        if behavior_logic is not None:
            self.behavior_logic = behavior_logic
        if features_engineering is not None:
            self.features_engineering = features_engineering
        if sample_param is not None:
            self.sample_param = sample_param
        if deep_learning_parameters is not None:
            self.deep_learning_parameters = deep_learning_parameters
        if algorithm_specify_parameters is not None:
            self.algorithm_specify_parameters = algorithm_specify_parameters
        if load_widetable is not None:
            self.load_widetable = load_widetable
        if load_profile is not None:
            self.load_profile = load_profile
        if save_mode is not None:
            self.save_mode = save_mode
        if indicators is not None:
            self.indicators = indicators
        if offline_rank_job_name is not None:
            self.offline_rank_job_name = offline_rank_job_name
        if update_interval is not None:
            self.update_interval = update_interval
        if optimizer is not None:
            self.optimizer = optimizer
        if flows is not None:
            self.flows = flows

    @property
    def nearline_recall_param(self):
        r"""Gets the nearline_recall_param of this JobConfig.

        :return: The nearline_recall_param of this JobConfig.
        :rtype: :class:`huaweicloudsdkres.v1.NearLineRecallParam`
        """
        return self._nearline_recall_param

    @nearline_recall_param.setter
    def nearline_recall_param(self, nearline_recall_param):
        r"""Sets the nearline_recall_param of this JobConfig.

        :param nearline_recall_param: The nearline_recall_param of this JobConfig.
        :type nearline_recall_param: :class:`huaweicloudsdkres.v1.NearLineRecallParam`
        """
        self._nearline_recall_param = nearline_recall_param

    @property
    def max_recommended_num(self):
        r"""Gets the max_recommended_num of this JobConfig.

        最大候选集个数（所有召回作业需提供此参数）。

        :return: The max_recommended_num of this JobConfig.
        :rtype: int
        """
        return self._max_recommended_num

    @max_recommended_num.setter
    def max_recommended_num(self, max_recommended_num):
        r"""Sets the max_recommended_num of this JobConfig.

        最大候选集个数（所有召回作业需提供此参数）。

        :param max_recommended_num: The max_recommended_num of this JobConfig.
        :type max_recommended_num: int
        """
        self._max_recommended_num = max_recommended_num

    @property
    def match_feature_pairs(self):
        r"""Gets the match_feature_pairs of this JobConfig.

        匹配特征对（属性匹配召回作业需要提供此参数）。

        :return: The match_feature_pairs of this JobConfig.
        :rtype: list[:class:`huaweicloudsdkres.v1.MatchFeaturePair`]
        """
        return self._match_feature_pairs

    @match_feature_pairs.setter
    def match_feature_pairs(self, match_feature_pairs):
        r"""Sets the match_feature_pairs of this JobConfig.

        匹配特征对（属性匹配召回作业需要提供此参数）。

        :param match_feature_pairs: The match_feature_pairs of this JobConfig.
        :type match_feature_pairs: list[:class:`huaweicloudsdkres.v1.MatchFeaturePair`]
        """
        self._match_feature_pairs = match_feature_pairs

    @property
    def striping(self):
        r"""Gets the striping of this JobConfig.

        :return: The striping of this JobConfig.
        :rtype: :class:`huaweicloudsdkres.v1.Striping`
        """
        return self._striping

    @striping.setter
    def striping(self, striping):
        r"""Sets the striping of this JobConfig.

        :param striping: The striping of this JobConfig.
        :type striping: :class:`huaweicloudsdkres.v1.Striping`
        """
        self._striping = striping

    @property
    def match_type(self):
        r"""Gets the match_type of this JobConfig.

        匹配类型（属性匹配召回作业需提供此参数）： - UI，基于用户推荐物品 - UU，基于用户推荐用户 - II，基于物品推荐物品 - IU，基于物品推荐用户

        :return: The match_type of this JobConfig.
        :rtype: str
        """
        return self._match_type

    @match_type.setter
    def match_type(self, match_type):
        r"""Sets the match_type of this JobConfig.

        匹配类型（属性匹配召回作业需提供此参数）： - UI，基于用户推荐物品 - UU，基于用户推荐用户 - II，基于物品推荐物品 - IU，基于物品推荐用户

        :param match_type: The match_type of this JobConfig.
        :type match_type: str
        """
        self._match_type = match_type

    @property
    def matrix_factorization(self):
        r"""Gets the matrix_factorization of this JobConfig.

        :return: The matrix_factorization of this JobConfig.
        :rtype: :class:`huaweicloudsdkres.v1.MatrixFactorization`
        """
        return self._matrix_factorization

    @matrix_factorization.setter
    def matrix_factorization(self, matrix_factorization):
        r"""Sets the matrix_factorization of this JobConfig.

        :param matrix_factorization: The matrix_factorization of this JobConfig.
        :type matrix_factorization: :class:`huaweicloudsdkres.v1.MatrixFactorization`
        """
        self._matrix_factorization = matrix_factorization

    @property
    def behavior_frequencys(self):
        r"""Gets the behavior_frequencys of this JobConfig.

        行为频率信息（历史行为记忆召回作业、历史行为过滤作业需提供此参数）。

        :return: The behavior_frequencys of this JobConfig.
        :rtype: list[:class:`huaweicloudsdkres.v1.BehaviorFrequency`]
        """
        return self._behavior_frequencys

    @behavior_frequencys.setter
    def behavior_frequencys(self, behavior_frequencys):
        r"""Sets the behavior_frequencys of this JobConfig.

        行为频率信息（历史行为记忆召回作业、历史行为过滤作业需提供此参数）。

        :param behavior_frequencys: The behavior_frequencys of this JobConfig.
        :type behavior_frequencys: list[:class:`huaweicloudsdkres.v1.BehaviorFrequency`]
        """
        self._behavior_frequencys = behavior_frequencys

    @property
    def file_path(self):
        r"""Gets the file_path of this JobConfig.

        文件路径（人工配置候选集作业需要提供此参数）。

        :return: The file_path of this JobConfig.
        :rtype: str
        """
        return self._file_path

    @file_path.setter
    def file_path(self, file_path):
        r"""Sets the file_path of this JobConfig.

        文件路径（人工配置候选集作业需要提供此参数）。

        :param file_path: The file_path of this JobConfig.
        :type file_path: str
        """
        self._file_path = file_path

    @property
    def ucb_param(self):
        r"""Gets the ucb_param of this JobConfig.

        :return: The ucb_param of this JobConfig.
        :rtype: :class:`huaweicloudsdkres.v1.UcbParam`
        """
        return self._ucb_param

    @ucb_param.setter
    def ucb_param(self, ucb_param):
        r"""Sets the ucb_param of this JobConfig.

        :param ucb_param: The ucb_param of this JobConfig.
        :type ucb_param: :class:`huaweicloudsdkres.v1.UcbParam`
        """
        self._ucb_param = ucb_param

    @property
    def behavior_gravity(self):
        r"""Gets the behavior_gravity of this JobConfig.

        :return: The behavior_gravity of this JobConfig.
        :rtype: :class:`huaweicloudsdkres.v1.BehaviorGravity`
        """
        return self._behavior_gravity

    @behavior_gravity.setter
    def behavior_gravity(self, behavior_gravity):
        r"""Sets the behavior_gravity of this JobConfig.

        :param behavior_gravity: The behavior_gravity of this JobConfig.
        :type behavior_gravity: :class:`huaweicloudsdkres.v1.BehaviorGravity`
        """
        self._behavior_gravity = behavior_gravity

    @property
    def category(self):
        r"""Gets the category of this JobConfig.

        :return: The category of this JobConfig.
        :rtype: :class:`huaweicloudsdkres.v1.Category`
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this JobConfig.

        :param category: The category of this JobConfig.
        :type category: :class:`huaweicloudsdkres.v1.Category`
        """
        self._category = category

    @property
    def behavior_logic(self):
        r"""Gets the behavior_logic of this JobConfig.

        行为逻辑过滤（历史行为过滤作业需提供此参数）： - AND，同时满足则过滤 - OR， 满足一个则过滤

        :return: The behavior_logic of this JobConfig.
        :rtype: str
        """
        return self._behavior_logic

    @behavior_logic.setter
    def behavior_logic(self, behavior_logic):
        r"""Sets the behavior_logic of this JobConfig.

        行为逻辑过滤（历史行为过滤作业需提供此参数）： - AND，同时满足则过滤 - OR， 满足一个则过滤

        :param behavior_logic: The behavior_logic of this JobConfig.
        :type behavior_logic: str
        """
        self._behavior_logic = behavior_logic

    @property
    def features_engineering(self):
        r"""Gets the features_engineering of this JobConfig.

        :return: The features_engineering of this JobConfig.
        :rtype: :class:`huaweicloudsdkres.v1.EtlBasicParameter`
        """
        return self._features_engineering

    @features_engineering.setter
    def features_engineering(self, features_engineering):
        r"""Sets the features_engineering of this JobConfig.

        :param features_engineering: The features_engineering of this JobConfig.
        :type features_engineering: :class:`huaweicloudsdkres.v1.EtlBasicParameter`
        """
        self._features_engineering = features_engineering

    @property
    def sample_param(self):
        r"""Gets the sample_param of this JobConfig.

        :return: The sample_param of this JobConfig.
        :rtype: :class:`huaweicloudsdkres.v1.SampleParam`
        """
        return self._sample_param

    @sample_param.setter
    def sample_param(self, sample_param):
        r"""Sets the sample_param of this JobConfig.

        :param sample_param: The sample_param of this JobConfig.
        :type sample_param: :class:`huaweicloudsdkres.v1.SampleParam`
        """
        self._sample_param = sample_param

    @property
    def deep_learning_parameters(self):
        r"""Gets the deep_learning_parameters of this JobConfig.

        :return: The deep_learning_parameters of this JobConfig.
        :rtype: :class:`huaweicloudsdkres.v1.DeepLearingParam`
        """
        return self._deep_learning_parameters

    @deep_learning_parameters.setter
    def deep_learning_parameters(self, deep_learning_parameters):
        r"""Sets the deep_learning_parameters of this JobConfig.

        :param deep_learning_parameters: The deep_learning_parameters of this JobConfig.
        :type deep_learning_parameters: :class:`huaweicloudsdkres.v1.DeepLearingParam`
        """
        self._deep_learning_parameters = deep_learning_parameters

    @property
    def algorithm_specify_parameters(self):
        r"""Gets the algorithm_specify_parameters of this JobConfig.

        :return: The algorithm_specify_parameters of this JobConfig.
        :rtype: :class:`huaweicloudsdkres.v1.AlgorithmSpecifyParameters`
        """
        return self._algorithm_specify_parameters

    @algorithm_specify_parameters.setter
    def algorithm_specify_parameters(self, algorithm_specify_parameters):
        r"""Sets the algorithm_specify_parameters of this JobConfig.

        :param algorithm_specify_parameters: The algorithm_specify_parameters of this JobConfig.
        :type algorithm_specify_parameters: :class:`huaweicloudsdkres.v1.AlgorithmSpecifyParameters`
        """
        self._algorithm_specify_parameters = algorithm_specify_parameters

    @property
    def load_widetable(self):
        r"""Gets the load_widetable of this JobConfig.

        导入宽表（离线数据导入作业需要提供此参数）。

        :return: The load_widetable of this JobConfig.
        :rtype: bool
        """
        return self._load_widetable

    @load_widetable.setter
    def load_widetable(self, load_widetable):
        r"""Sets the load_widetable of this JobConfig.

        导入宽表（离线数据导入作业需要提供此参数）。

        :param load_widetable: The load_widetable of this JobConfig.
        :type load_widetable: bool
        """
        self._load_widetable = load_widetable

    @property
    def load_profile(self):
        r"""Gets the load_profile of this JobConfig.

        导入画像（离线数据导入作业需要提供此参数）。

        :return: The load_profile of this JobConfig.
        :rtype: bool
        """
        return self._load_profile

    @load_profile.setter
    def load_profile(self, load_profile):
        r"""Sets the load_profile of this JobConfig.

        导入画像（离线数据导入作业需要提供此参数）。

        :param load_profile: The load_profile of this JobConfig.
        :type load_profile: bool
        """
        self._load_profile = load_profile

    @property
    def save_mode(self):
        r"""Gets the save_mode of this JobConfig.

        保留已有宽表（离线数据导入作业需要提供此参数）： - append，是 - new，否 - overwirte，覆盖

        :return: The save_mode of this JobConfig.
        :rtype: str
        """
        return self._save_mode

    @save_mode.setter
    def save_mode(self, save_mode):
        r"""Sets the save_mode of this JobConfig.

        保留已有宽表（离线数据导入作业需要提供此参数）： - append，是 - new，否 - overwirte，覆盖

        :param save_mode: The save_mode of this JobConfig.
        :type save_mode: str
        """
        self._save_mode = save_mode

    @property
    def indicators(self):
        r"""Gets the indicators of this JobConfig.

        统计指标（效果评估作业需要提供此参数）。

        :return: The indicators of this JobConfig.
        :rtype: list[:class:`huaweicloudsdkres.v1.Indicator`]
        """
        return self._indicators

    @indicators.setter
    def indicators(self, indicators):
        r"""Sets the indicators of this JobConfig.

        统计指标（效果评估作业需要提供此参数）。

        :param indicators: The indicators of this JobConfig.
        :type indicators: list[:class:`huaweicloudsdkres.v1.Indicator`]
        """
        self._indicators = indicators

    @property
    def offline_rank_job_name(self):
        r"""Gets the offline_rank_job_name of this JobConfig.

        离线排序作业名称（在线训练任务需要提供此参数）。

        :return: The offline_rank_job_name of this JobConfig.
        :rtype: str
        """
        return self._offline_rank_job_name

    @offline_rank_job_name.setter
    def offline_rank_job_name(self, offline_rank_job_name):
        r"""Sets the offline_rank_job_name of this JobConfig.

        离线排序作业名称（在线训练任务需要提供此参数）。

        :param offline_rank_job_name: The offline_rank_job_name of this JobConfig.
        :type offline_rank_job_name: str
        """
        self._offline_rank_job_name = offline_rank_job_name

    @property
    def update_interval(self):
        r"""Gets the update_interval of this JobConfig.

        更新周期（在线训练任务需要提供此参数）。

        :return: The update_interval of this JobConfig.
        :rtype: int
        """
        return self._update_interval

    @update_interval.setter
    def update_interval(self, update_interval):
        r"""Sets the update_interval of this JobConfig.

        更新周期（在线训练任务需要提供此参数）。

        :param update_interval: The update_interval of this JobConfig.
        :type update_interval: int
        """
        self._update_interval = update_interval

    @property
    def optimizer(self):
        r"""Gets the optimizer of this JobConfig.

        :return: The optimizer of this JobConfig.
        :rtype: :class:`huaweicloudsdkres.v1.Optimizer`
        """
        return self._optimizer

    @optimizer.setter
    def optimizer(self, optimizer):
        r"""Sets the optimizer of this JobConfig.

        :param optimizer: The optimizer of this JobConfig.
        :type optimizer: :class:`huaweicloudsdkres.v1.Optimizer`
        """
        self._optimizer = optimizer

    @property
    def flows(self):
        r"""Gets the flows of this JobConfig.

        :return: The flows of this JobConfig.
        :rtype: :class:`huaweicloudsdkres.v1.Flow`
        """
        return self._flows

    @flows.setter
    def flows(self, flows):
        r"""Sets the flows of this JobConfig.

        :param flows: The flows of this JobConfig.
        :type flows: :class:`huaweicloudsdkres.v1.Flow`
        """
        self._flows = flows

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
        if not isinstance(other, JobConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
