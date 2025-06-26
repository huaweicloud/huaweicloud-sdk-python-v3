# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSimSimulationsFilesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'algorithm_log_url': 'str',
        'algorithm_pb_url': 'str',
        'algorithm_meta_url': 'str',
        'sim_osi_url': 'str',
        'osi_meta_url': 'str',
        'evaluation_url': 'str',
        'evaluation_log_url': 'str'
    }

    attribute_map = {
        'algorithm_log_url': 'algorithm_log_url',
        'algorithm_pb_url': 'algorithm_pb_url',
        'algorithm_meta_url': 'algorithm_meta_url',
        'sim_osi_url': 'sim_osi_url',
        'osi_meta_url': 'osi_meta_url',
        'evaluation_url': 'evaluation_url',
        'evaluation_log_url': 'evaluation_log_url'
    }

    def __init__(self, algorithm_log_url=None, algorithm_pb_url=None, algorithm_meta_url=None, sim_osi_url=None, osi_meta_url=None, evaluation_url=None, evaluation_log_url=None):
        r"""ShowSimSimulationsFilesResponse

        The model defined in huaweicloud sdk

        :param algorithm_log_url: 算法日志下载地址
        :type algorithm_log_url: str
        :param algorithm_pb_url: 算法pb文件下载地址
        :type algorithm_pb_url: str
        :param algorithm_meta_url: 算法pb文件元数据下载地址
        :type algorithm_meta_url: str
        :param sim_osi_url: 仿真pb文件下载地址
        :type sim_osi_url: str
        :param osi_meta_url: 仿真pb文件元数据下载地址
        :type osi_meta_url: str
        :param evaluation_url: 评测pb文件下载地址
        :type evaluation_url: str
        :param evaluation_log_url: 评测日志下载地址
        :type evaluation_log_url: str
        """
        
        super(ShowSimSimulationsFilesResponse, self).__init__()

        self._algorithm_log_url = None
        self._algorithm_pb_url = None
        self._algorithm_meta_url = None
        self._sim_osi_url = None
        self._osi_meta_url = None
        self._evaluation_url = None
        self._evaluation_log_url = None
        self.discriminator = None

        if algorithm_log_url is not None:
            self.algorithm_log_url = algorithm_log_url
        if algorithm_pb_url is not None:
            self.algorithm_pb_url = algorithm_pb_url
        if algorithm_meta_url is not None:
            self.algorithm_meta_url = algorithm_meta_url
        if sim_osi_url is not None:
            self.sim_osi_url = sim_osi_url
        if osi_meta_url is not None:
            self.osi_meta_url = osi_meta_url
        if evaluation_url is not None:
            self.evaluation_url = evaluation_url
        if evaluation_log_url is not None:
            self.evaluation_log_url = evaluation_log_url

    @property
    def algorithm_log_url(self):
        r"""Gets the algorithm_log_url of this ShowSimSimulationsFilesResponse.

        算法日志下载地址

        :return: The algorithm_log_url of this ShowSimSimulationsFilesResponse.
        :rtype: str
        """
        return self._algorithm_log_url

    @algorithm_log_url.setter
    def algorithm_log_url(self, algorithm_log_url):
        r"""Sets the algorithm_log_url of this ShowSimSimulationsFilesResponse.

        算法日志下载地址

        :param algorithm_log_url: The algorithm_log_url of this ShowSimSimulationsFilesResponse.
        :type algorithm_log_url: str
        """
        self._algorithm_log_url = algorithm_log_url

    @property
    def algorithm_pb_url(self):
        r"""Gets the algorithm_pb_url of this ShowSimSimulationsFilesResponse.

        算法pb文件下载地址

        :return: The algorithm_pb_url of this ShowSimSimulationsFilesResponse.
        :rtype: str
        """
        return self._algorithm_pb_url

    @algorithm_pb_url.setter
    def algorithm_pb_url(self, algorithm_pb_url):
        r"""Sets the algorithm_pb_url of this ShowSimSimulationsFilesResponse.

        算法pb文件下载地址

        :param algorithm_pb_url: The algorithm_pb_url of this ShowSimSimulationsFilesResponse.
        :type algorithm_pb_url: str
        """
        self._algorithm_pb_url = algorithm_pb_url

    @property
    def algorithm_meta_url(self):
        r"""Gets the algorithm_meta_url of this ShowSimSimulationsFilesResponse.

        算法pb文件元数据下载地址

        :return: The algorithm_meta_url of this ShowSimSimulationsFilesResponse.
        :rtype: str
        """
        return self._algorithm_meta_url

    @algorithm_meta_url.setter
    def algorithm_meta_url(self, algorithm_meta_url):
        r"""Sets the algorithm_meta_url of this ShowSimSimulationsFilesResponse.

        算法pb文件元数据下载地址

        :param algorithm_meta_url: The algorithm_meta_url of this ShowSimSimulationsFilesResponse.
        :type algorithm_meta_url: str
        """
        self._algorithm_meta_url = algorithm_meta_url

    @property
    def sim_osi_url(self):
        r"""Gets the sim_osi_url of this ShowSimSimulationsFilesResponse.

        仿真pb文件下载地址

        :return: The sim_osi_url of this ShowSimSimulationsFilesResponse.
        :rtype: str
        """
        return self._sim_osi_url

    @sim_osi_url.setter
    def sim_osi_url(self, sim_osi_url):
        r"""Sets the sim_osi_url of this ShowSimSimulationsFilesResponse.

        仿真pb文件下载地址

        :param sim_osi_url: The sim_osi_url of this ShowSimSimulationsFilesResponse.
        :type sim_osi_url: str
        """
        self._sim_osi_url = sim_osi_url

    @property
    def osi_meta_url(self):
        r"""Gets the osi_meta_url of this ShowSimSimulationsFilesResponse.

        仿真pb文件元数据下载地址

        :return: The osi_meta_url of this ShowSimSimulationsFilesResponse.
        :rtype: str
        """
        return self._osi_meta_url

    @osi_meta_url.setter
    def osi_meta_url(self, osi_meta_url):
        r"""Sets the osi_meta_url of this ShowSimSimulationsFilesResponse.

        仿真pb文件元数据下载地址

        :param osi_meta_url: The osi_meta_url of this ShowSimSimulationsFilesResponse.
        :type osi_meta_url: str
        """
        self._osi_meta_url = osi_meta_url

    @property
    def evaluation_url(self):
        r"""Gets the evaluation_url of this ShowSimSimulationsFilesResponse.

        评测pb文件下载地址

        :return: The evaluation_url of this ShowSimSimulationsFilesResponse.
        :rtype: str
        """
        return self._evaluation_url

    @evaluation_url.setter
    def evaluation_url(self, evaluation_url):
        r"""Sets the evaluation_url of this ShowSimSimulationsFilesResponse.

        评测pb文件下载地址

        :param evaluation_url: The evaluation_url of this ShowSimSimulationsFilesResponse.
        :type evaluation_url: str
        """
        self._evaluation_url = evaluation_url

    @property
    def evaluation_log_url(self):
        r"""Gets the evaluation_log_url of this ShowSimSimulationsFilesResponse.

        评测日志下载地址

        :return: The evaluation_log_url of this ShowSimSimulationsFilesResponse.
        :rtype: str
        """
        return self._evaluation_log_url

    @evaluation_log_url.setter
    def evaluation_log_url(self, evaluation_log_url):
        r"""Sets the evaluation_log_url of this ShowSimSimulationsFilesResponse.

        评测日志下载地址

        :param evaluation_log_url: The evaluation_log_url of this ShowSimSimulationsFilesResponse.
        :type evaluation_log_url: str
        """
        self._evaluation_log_url = evaluation_log_url

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
        if not isinstance(other, ShowSimSimulationsFilesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
